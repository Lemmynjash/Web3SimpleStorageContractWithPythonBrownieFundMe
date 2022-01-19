from brownie import network, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 2000
LOCAL_BLOCHAIN_ENVIRONMENT = ["development", "ganache-local"]


def getaccounts():
    if network.show_active() in LOCAL_BLOCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.load("lemmy-account")


def deploy_mocks():
    print("Deploying Mocks.....")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": getaccounts()})
