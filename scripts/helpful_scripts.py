from brownie import network, accounts


def getaccounts():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("lemmy-account")
