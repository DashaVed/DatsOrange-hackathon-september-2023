from random import randint

from utils.api_requests import sell_stock, PRICE_TO_BUY, limit_price_buy, limit_price_sell
from utils.cleaning import clean_stock, get_cheap_asset, get_now_oranges


def buy_cheapest_assets():
    ticker_id = -1
    min_price = PRICE_TO_BUY
    now_quantity = 0

    assets = clean_stock(sell_stock())
    for asset in assets:
        price, quantity = get_cheap_asset(asset)
        if price < min_price:
            ticker_id = asset["id"]
            min_price = price
            now_quantity = quantity
        elif price == min_price:
            ticker_id = asset["id"]
            now_quantity = max(quantity, now_quantity)

    quantity_to_buy = get_now_oranges() // min_price
    if quantity_to_buy > 0:
        limit_price_buy(symbol_id=ticker_id, price=min_price, quantity=quantity_to_buy)
        limit_price_sell(symbol_id=ticker_id, price=min_price + randint(10, 100), quantity=quantity_to_buy)
    else:
        print("Апельсины закончились :D")


if __name__ == "__main__":
    print("Попытка купить дешевые акции")
    buy_cheapest_assets()
