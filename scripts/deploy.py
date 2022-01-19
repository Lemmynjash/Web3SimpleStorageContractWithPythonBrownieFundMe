from brownie import FundMe, network, config, MockV3Aggregator
import scripts.helpful_scripts as hp


def deploy_fund_me():
    account = hp.getaccounts()

    # if we are on a persistent network like rinkeby,use the associated address
    # otherwise deploy mocks(this is a deployed fake version for interaction)
    if network.show_active() not in hp.LOCAL_BLOCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active(
        )]["eth_usd_price_list"]
    else:
        print(f" The active netork is {network.show_active()}")
        hp.deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks Deployed.....")

    fund_me = FundMe.deploy(price_feed_address,
                            {"from": account},
                            publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
