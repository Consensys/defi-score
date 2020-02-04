from . import constants, pool_data_service, finance_service
import math, json


def calculate_score(protocol, token, liquidity_value, collateral_value):
    if protocol == 'dydx':
        protocol_values = constants.dydx_values
    elif protocol == 'compound':
        protocol_values = constants.compound_values
    elif protocol == 'fulcrum':
        protocol_values = constants.fulcrum_values
    elif protocol == 'nuo':
        protocol_values = constants.nuo_values
    else:
        protocol_values = constants.ddex_values
    
    weights = constants.weights
    score = weights['auditedCode'] * protocol_values['isCodeAudited'] + weights['allCodeOSS'] * protocol_values['isCodeOpenSource'] + weights['formalVer'] * protocol_values['isCodeFormallyVerified'] + weights['hasBugBounty'] * protocol_values['hasBugBounty'] + weights['cVaR'] * protocol_values['cvar'] + weights['poolCollateralization'] * collateral_value + weights['poolLiquidity'] * liquidity_value + weights['centralizationRisk'] * protocol_values['centralizationRisk']
    score = round(score, 2) * 10
    score = "{:.1f}".format(score)
    result = {
        'asset': token,
        'protocol': protocol,
        'metrics': {
            'score': score,
            'liquidityIndex': str(liquidity_value),
            'collateralIndex': str(collateral_value)
        }
    }
    return result

def calculate_scores():
    # Get all pool data
    all_pool_data = pool_data_service.fetch_data_for_all_pools()
    test = [p for p in all_pool_data if p['liquidity'] == 0]
    liquidity_array = [math.log(p['liquidity']) for p in all_pool_data]
    utilization_array = [p['utilizationRate'] for p in all_pool_data]
    results = []
    for data in all_pool_data:
        liquidity_value = finance_service.normalize_data(math.log(data['liquidity']), liquidity_array)
        # Subtracting from 1 because lower utilization is safer
        utilization_value = 1 - finance_service.normalize_data(data['utilizationRate'], utilization_array)
        score = calculate_score(data['protocol'], data['token'], liquidity_value, utilization_value)
        results.append(score)
    return results

def main():
  print('Beginning score calculation...')

  # Pulling and calculating Compound data
  compound_tokens = [x['token'] for x in constants.compoundContractInfo]
  compound_balances = [pool_data_service.fetch_data_for_pool('compound', t) for t in compound_tokens]
  compound_portfolio_cvar = finance_service.generate_cvar_from_balances(compound_balances)
  # add instead of subtract here because cvar from this function is negative
  constants.compound_values['cvar'] = 1 + compound_portfolio_cvar

  # Pulling and calculating dYdX data
  dydx_tokens = constants.dydxContractInfo['activeMarkets']
  dydx_balances = [pool_data_service.fetch_data_for_pool('dydx', t) for t in dydx_tokens]
  dydx_portfolio_cvar = finance_service.generate_cvar_from_balances(dydx_balances)
  # add instead of subtract here because cvar from this function is negative
  constants.dydx_values['cvar'] = 1 + dydx_portfolio_cvar

  # Pulling and calculating Fulcrum data
  fulcrum_tokens = [x['token'] for x in constants.fulcrumContractInfo]
  fulcrum_balances = [pool_data_service.fetch_data_for_pool('fulcrum', t) for t in fulcrum_tokens]
  fulcrum_portfolio_cvar = finance_service.generate_cvar_from_balances(fulcrum_balances)
  # add instead of subtract here because cvar from this function is negative
  constants.fulcrum_values['cvar'] = 1 + fulcrum_portfolio_cvar

  # Pulling and calculating Nuo data
  nuo_tokens = [x['token'] for x in constants.nuoContractInfo]
  nuo_balances = [pool_data_service.fetch_data_for_pool('nuo', t) for t in nuo_tokens]
  nuo_portfolio_cvar = finance_service.generate_cvar_from_balances(nuo_balances)
  # add instead of subtract here because cvar from this function is negative
  constants.nuo_values['cvar'] = 1 + nuo_portfolio_cvar

  # Pulling and calculating DDEX data
  ddex_tokens = [x['token'] for x in constants.ddexContractInfo]
  ddex_balances = [pool_data_service.fetch_data_for_pool('ddex', t) for t in ddex_tokens]
  ddex_portfolio_cvar = finance_service.generate_cvar_from_balances(ddex_balances)
  # add instead of subtract here because cvar from this function is negative
  constants.ddex_values['cvar'] = 1 + ddex_portfolio_cvar

  scores = calculate_scores()

  scores.append({
    'asset': 'dai',
    'protocol': 'mcd',
    'metrics': {
      'score': 9.7
    }
  })

  with open('./implementation/data.json', 'w', encoding='utf-8') as f:
      json.dump(scores, f, ensure_ascii=False, indent=4)
  
  print('Score calculation finished!')

main()