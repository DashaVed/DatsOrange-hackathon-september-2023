import time

from utils import info, limit_price_sell, PRICE_TO_SELL


def sell_all_assets_from_account():
    account_data = info()
    for asset in account_data["assets"]:
        if asset["id"] != 1 and asset["quantity"] != 0:
            limit_price_sell(symbol_id=asset["id"], price=PRICE_TO_SELL, quantity=asset["quantity"])


while True:
    sell_all_assets_from_account()
    time.sleep(60)
