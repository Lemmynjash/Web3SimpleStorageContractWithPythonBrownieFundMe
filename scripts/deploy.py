from brownie import FundMe
import scripts.helpful_scripts as hp


def deploy_fund_me():
    account = hp.getaccounts()
    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
