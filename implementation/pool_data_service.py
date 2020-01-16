from . import web3_service, constants
import json, requests
from pprint import pprint

# PRIVATE FUNCTIONS #
def fetch_current_usd_value(token):
    if (token[0] == 'i' and token[1] == 'w'):
        token_ticker = token[2:].upper()
    elif (token[0] == 'c' or token[0] ==  'w' or token[0] == 'i'):
        token_ticker = token[1:].upper()
    elif token == 'sai':
      token_ticker = 'DAI'
    else:
        token_ticker = token.upper()
    result = requests.get(f'https://min-api.cryptocompare.com/data/dayAvg?fsym={token_ticker}&tsym=USD')
    json = result.json()
    return json['USD']

def create_pool_data_object(token, total_supply, total_borrow, collateral=0):
  usd_price = fetch_current_usd_value(token)
  liquidity_base_token = total_supply - total_borrow
  utilization_rate = total_borrow / total_supply
  collateral_base_token = collateral if collateral != 0 else liquidity_base_token
  pool_data = {
    'liquidity': liquidity_base_token * usd_price,
    'liquidityBaseToken': liquidity_base_token,
    'collateral': collateral_base_token  * usd_price,
    'collateralBaseToken': collateral_base_token,
    'totalSupply': total_supply * usd_price,
    'totalSupplyBaseToken': total_supply,
    'totalBorrow': total_borrow  * usd_price,
    'totalBorrowBaseToken': total_borrow,
    'utilizationRate': utilization_rate
  }
  return pool_data

def get_all_available_pools():
    all_available_pools = []
    for t in constants.dydxContractInfo['activeMarkets']:
      all_available_pools.append({ 'protocol': 'dydx', 'token': t })
    for t in constants.compoundContractInfo:
      all_available_pools.append({ 'protocol': 'compound', 'token': t['token'] })
    for t in constants.fulcrumContractInfo:
      all_available_pools.append({ 'protocol': 'fulcrum', 'token': t['token'] })
    for t in constants.nuoContractInfo:
      all_available_pools.append({ 'protocol': 'nuo', 'token': t['token'] })
    for t in constants.ddexContractInfo:
      all_available_pools.append({ 'protocol': 'ddex', 'token': t['token'] })
    for t in constants.aaveContractInfo:
      all_available_pools.append({ 'protocol': 'aave', 'token': t['token'] })
    return all_available_pools

def fetch_data_for_nuo_pool(token):
  # Have to fetch the data from the API for now because fetching outstandingDebt from Nuo is challenging
  nuo_data = requests.get('https://api.nuoscan.io/overview').json()['data']
  pool_data = next((p for p in nuo_data['reserves'] if p['currency']['short_name'] == token.upper()))
  total_supply = pool_data['total_balance']
  total_borrow = pool_data['active_loan_amount_sum']
  result = create_pool_data_object(token, total_supply, total_borrow)
  return result
  
def fetch_data_for_compound_pool(token):
  pool_info = next((m for m in constants.compoundContractInfo if m['token'] == token))
  shift_by = web3_service.findDecimals(pool_info['token'])
  abi = json.loads(constants.compound_ceth_abi_string) if (pool_info['token'] == 'eth') else json.loads(constants.erc20_abi_string)
  initialized_contract = web3_service.initializeContract(address=pool_info['contract'], abi=abi)
  # Grabs liquidity from contract which needs to be transformed according to decimals
  liquidity = initialized_contract.functions.getCash().call() / 10 ** shift_by
  total_borrow = initialized_contract.functions.totalBorrows().call() / 10 ** shift_by
  total_supply = liquidity + total_borrow
  result = create_pool_data_object(token, total_supply, total_borrow)
  return result

def fetch_data_for_dydx_pool(token):
    shift_by = 6 if token == 'usdc'  else 18
    pool_info = constants.dydxContractInfo['markets'].index(token)
    initializedContract = web3_service.initializeContract(constants.dydxContractInfo['contractAddress'], abi=constants.dydx_abi_string)
    pool_data = initializedContract.functions.getMarketWithInfo(pool_info).call()
    # Grab + calculate data from dydx market info structure
    total_supply = pool_data[0][1][1] / 10 ** shift_by
    total_borrow = pool_data[0][1][0] / 10 ** shift_by
    result = create_pool_data_object(token, total_supply, total_borrow)
    return result


def fetch_data_for_fulcrum_pool(token):
  shift_by = web3_service.findDecimals(token)
  pool_info = next((m for m in constants.fulcrumContractInfo if m['token'] == token))
  itoken_contract = web3_service.initializeContract(pool_info['contractAddress'], constants.fulcrum_itoken_abi)
  total_supply = itoken_contract.functions.totalAssetSupply().call() / 10 ** shift_by
  total_borrow = itoken_contract.functions.totalAssetBorrow().call() / 10 ** shift_by
  result = create_pool_data_object(token, total_supply, total_borrow)
  return result

def fetch_data_for_ddex_pool(token):
  shift_by = web3_service.findDecimals(token)
  pool_info = next((m for m in constants.ddexContractInfo if m['token'] == token))
  ddex_contract_address = web3_service.w3.toChecksumAddress(constants.ddex_address)
  ddex_contract = web3_service.initializeContract(constants.ddex_address, constants.ddex_abi)
  checksummed_base_token_address = web3_service.w3.toChecksumAddress(pool_info['baseTokenAddress'])
  base_token_contract = web3_service.initializeContract(pool_info['baseTokenAddress'], constants.erc20_abi_string)
  if (token == 'eth'):
    collateral = web3_service.w3.eth.getBalance(ddex_contract_address) / 10 ** shift_by
  else:
    collateral = base_token_contract.functions.balanceOf(ddex_contract_address).call() / 10 ** shift_by
  total_supply = ddex_contract.functions.getTotalSupply(checksummed_base_token_address).call() / 10 ** shift_by
  total_borrow = ddex_contract.functions.getTotalBorrow(checksummed_base_token_address).call() / 10 ** shift_by
  result = create_pool_data_object(token, total_supply, total_borrow, collateral)
  return result

def fetch_data_for_aave_pool(token):
  shift_by = web3_service.findDecimals(token)
  pool_info = next((m for m in constants.aaveContractInfo if m['token'] == token))
  aave_contract_address = web3_service.w3.toChecksumAddress(constants.aave_address)
  checksummed_base_token_address = web3_service.w3.toChecksumAddress(pool_info['baseTokenAddress'])
  aave_contract = web3_service.initializeContract(aave_contract_address, constants.aave_abi)
  market_info = aave_contract.functions.getReserveData(checksummed_base_token_address).call()
  pprint(market_info)
  total_supply = market_info[0] / 10 ** shift_by
  total_borrow_stable = market_info[2] / 10 ** shift_by
  total_borrows_variable = market_info[3] / 10 ** shift_by
  total_borrow = total_borrow_stable + total_borrows_variable
  result = create_pool_data_object(token, total_supply, total_borrow)
  return result

# PUBLIC FUNCTIONS #
def fetch_data_for_pool(protocol, token, block='latest'):
  if protocol == 'compound':
    result = fetch_data_for_compound_pool(token)
  elif protocol == 'dydx':
    result = fetch_data_for_dydx_pool(token)
  elif protocol == 'fulcrum':
    result = fetch_data_for_fulcrum_pool(token)
  elif protocol == 'nuo':
    result = fetch_data_for_nuo_pool(token)
  elif protocol == 'aave':
    result = fetch_data_for_aave_pool(token)
  else:
    result = fetch_data_for_ddex_pool(token)
  result['protocol'] = protocol
  result['token'] = token
  return result
    

def fetch_data_for_all_pools(block="latest"):
  all_pools = get_all_available_pools()
  result = []
  for pool in all_pools:
    pool_data = fetch_data_for_pool(pool['protocol'], pool['token'])
    result.append(pool_data)
  return result
  