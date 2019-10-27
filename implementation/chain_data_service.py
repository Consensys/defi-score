import web3_service, constants, json, requests

# Used to find current USD values for all coins
def findCurrentUSDValue(token):
    tokenTicker = ''
    if (token[0] == 'i' and token[1] == 'w'):
        tokenTicker = token[2:].upper()
    elif (token[0] == 'c' or token[0] ==  'w' or token[0] == 'i'):
        tokenTicker = token[1:].upper()
    else:
        tokenTicker = token.upper()
    result = requests.get(f'https://min-api.cryptocompare.com/data/dayAvg?fsym={tokenTicker}&tsym=USD')
    json = result.json()
    return json['USD']

def fetch_data_for_nuo_market(market):
  shiftBy = web3_service.findDecimals(market['token'])
  reserve_contract = web3_service.initializeContract(constants.nuo_reserve_address, constants.nuo_reserve_abi)
  base_token_contract = web3_service.initializeContract(market['baseTokenAddress'], abi=constants.erc20_abi_string)
  checksummed_kernel_address = web3_service.w3.toChecksumAddress(constants.nuo_kernel_address)
  checksummed_base_token_address =  web3_service.w3.toChecksumAddress(market['baseTokenAddress'])
  nuo_kernel_raw_balance = base_token_contract.functions.balanceOf(checksummed_kernel_address).call()
  last_reserve_run = reserve_contract.functions.lastReserveRuns(checksummed_base_token_address).call()
  nuo_reserve_raw_balance = reserve_contract.functions.reserves(last_reserve_run, checksummed_base_token_address).call()
  raw_balance = nuo_reserve_raw_balance + nuo_kernel_raw_balance
  balance = raw_balance / 10**shiftBy
  usd_value = findCurrentUSDValue(market['token'])
  balance_value = balance * usd_value
  market['amount'] = balance
  market['balance'] = balance_value
  return market
  
def fetch_data_for_compound_market(market):
  shiftBy = web3_service.findDecimals(market['token'])
  abi = json.loads(constants.compound_ceth_abi_string) if (market['token'] == 'eth') else json.loads(constants.erc20_abi_string)
  initializedContract = web3_service.initializeContract(address=market['contract'], abi=abi)
  # This grabs liquidity from contract which needs to be transformed according to decimals
  rawLiquidity = initializedContract.functions.getCash().call()
  liquidity = rawLiquidity / 10**shiftBy
  # This grabs outstanding from contract which needs to be transformed according to decimals
  rawOutstandingDebt = initializedContract.functions.totalBorrows().call()
  outstandingDebt = rawOutstandingDebt / 10**shiftBy
  # Total supply should be liquidity + outstanding debt
  totalSupply = liquidity + outstandingDebt
  usdValue = findCurrentUSDValue(market['token'])
  market['amount'] = liquidity
  market['balance'] = liquidity * usdValue
  market['liquidityValue'] = liquidity * usdValue
  market['totalBorrowValue'] = outstandingDebt * usdValue
  market['totalSupplyValue'] = totalSupply * usdValue
  return market

def fetch_data_for_dydx_market(market):
    shiftBy = 6 if market == 2 else 18
    token = constants.dydxContractInfo['markets'][market]
    initializedContract = web3_service.initializeContract(constants.dydxContractInfo['contractAddress'], abi=constants.dydx_abi_string)
    marketData = initializedContract.functions.getMarketWithInfo(market).call()
    # Grab supply and borrow from dydx market info data structure
    totalSupply = marketData[0][1][1] / 10 ** shiftBy
    outstandingDebt = marketData[0][1][0] / 10 ** shiftBy
    # Then calculate liquidity
    liquidity = totalSupply - outstandingDebt
    usdValue = findCurrentUSDValue(constants.dydxContractInfo['markets'][market])
    result = {}
    result['token'] = constants.dydxContractInfo['markets'][market]
    result['amount'] = liquidity
    result['balance'] = liquidity * usdValue
    result['liquidity'] = liquidity * usdValue
    result['totalSupplyValue'] = totalSupply * usdValue
    result['totalBorrowValue'] = outstandingDebt * usdValue
    return result


def fetch_data_for_fulcrum_market(market):
  shiftBy = web3_service.findDecimals(market['token'])
  itoken_contract = web3_service.initializeContract(market['contractAddress'], constants.fulcrum_itoken_abi)
  base_token_contract = web3_service.initializeContract(market['baseTokenAddress'], abi=constants.erc20_abi_string)
  itoken_liquidity_raw = itoken_contract.functions.marketLiquidity().call()
  base_token_collateral = base_token_contract.functions.balanceOf(constants.bzx_valut_address).call()
  liquidity = itoken_liquidity_raw / 10 ** shiftBy
  usdValue = findCurrentUSDValue(market['token'])
  market['amount'] = liquidity
  market['balance'] = liquidity * usdValue
  market['liquidity'] = liquidity
  market['liquidityValue'] = liquidity * usdValue
  return market