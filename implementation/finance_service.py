import json, requests, time, math
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
from functools import reduce
from . import constants, web3_service, pool_data_service

# Used to find portfolio weights for an array of balances
def getWeights(balances):
    total = 0
    weights = []
    for balance in balances:
        total += balance['liquidity']
    for balance in balances:
        percentage = balance['liquidity']/total
        weights.append(percentage)
    return weights

# Used to find historical USD values for stablecoins
def getCryptoCompareReturns(token):
    result = requests.get(f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={token}&tsym=USD&limit=720')
    json = result.json()
    df = pd.DataFrame([object for object in json['Data']['Data']])
    df.insert(0, 'Date', pd.to_datetime(df['time'],unit='s'))
    df.drop(['high', 'open', 'low', 'volumefrom', 'volumeto', 'conversionType', 'conversionSymbol', 'time'], axis=1, inplace=True)
    df.set_index('Date', inplace=True)
    returns = df.copy().pct_change().fillna(value=0, axis=0).rename(columns={'close': f'daily_returns_{token}'})
    return returns
    
# TODO - Fix Dates
# Used to find historical USD values for all coins but stablecoins      
def getReturns(tokens): 
    last_date = datetime.today().strftime('%Y-%m-%d')
    first_date = (datetime.today() - timedelta(days=520)).strftime('%Y-%m-%d')
    df_list = []
    for token in tokens:
        if (token['token'] == 'wbtc'):
            token = token['token'][1:].upper()
        else:
            token = token['token'].upper()
        if (token == 'DAI' or token == 'USDC' or token == 'MKR' or token == 'TUSD' or token == 'USDT' or token == 'SAI'):
            if token == 'SAI':
                token = 'DAI'
            ticker_returns = getCryptoCompareReturns(token)
            df_list.append(ticker_returns)
        else:
            ticker = f'{token}-USD'
            ticker_close = pdr.get_data_yahoo(ticker, first_date, last_date)[['Close']]
            ticker_returns = ticker_close.copy().pct_change().fillna(value=0, axis=0).rename(columns={'Close': f'daily_returns_{token}'})
            df_list.append(ticker_returns)
    df = reduce(lambda x, y: pd.merge(x, y, on = 'Date'), df_list)
    return df

def value_at_risk(returns, weights, alpha=0.95, lookback_days=520):
    # Multiply asset returns by weights to get one weighted portfolio return
    portfolio_returns = returns.iloc[-lookback_days:].dot(weights)
    # Compute the correct percentile loss and multiply by value invested
    return np.percentile(portfolio_returns, 100 * (1-alpha))

def cvar(returns, weights, alpha=0.95, lookback_days=520):
    var = value_at_risk(returns, weights, alpha, lookback_days=lookback_days)
    returns = returns.fillna(0.0)
    portfolio_returns = returns.iloc[-lookback_days:].dot(weights)
    # Get back to a return rather than an absolute loss
    var_pct_loss = var / 1
    return np.nanmean(portfolio_returns[portfolio_returns < var_pct_loss])

def generate_cvar_from_balances(balances):
    weights = getWeights(balances)
    returns = getReturns(balances)
    returns = returns.fillna(0.0)
    portfolio_returns = returns.fillna(0.0).iloc[-520:].dot(weights)
    portfolio_cvar = cvar(returns, weights, 0.99, 520)
    return portfolio_cvar

def EMACalc(m_array, m_range):
    k = 2/(m_range + 1)
    # first item is just the same as the first item in the input
    ema_array = [m_array[0]]
    # for the rest of the items, they are computed with the previous one
    i = 1
    while i < m_range:
        ema_array.append(m_array[i] * k + ema_array[i - 1] * (1 - k))
        i += 1
    return ema_array[len(ema_array) - 1]

# Normalize value from a list of objects with predefined shape
def normalize_data(val, list):
    max_value = max(list)
    min_value = min(list)
    return (val - min_value) / (max_value - min_value)