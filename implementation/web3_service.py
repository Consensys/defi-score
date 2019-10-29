import os
from web3 import Web3
from dotenv import load_dotenv
load_dotenv(verbose=True)

INFURA_API_KEY = os.getenv("INFURA_API_KEY")

# Setup web3
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'))

def initializeContract(address, abi):
  checksummed_address = w3.toChecksumAddress(address)
  contract = w3.eth.contract(address=checksummed_address, abi=abi)
  return contract

# Used to find decimals value for a token
def findDecimals(token): 
    decimals = 0
    if (token == 'wbtc'):
        decimals = 8
    elif (token == 'usdc'):
        decimals = 6
    else:
        decimals = 18
    return decimals

