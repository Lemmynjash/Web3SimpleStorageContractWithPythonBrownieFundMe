from brownie import FundMe
import scripts.helpful_scripts as hp


def fund():
    fund_me = FundMe[-1]
    account = hp.getaccounts()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The Entrance fee is {entrance_fee}")
    print("Funding me now ...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = hp.getaccounts()
    print("Withdraw now ...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
