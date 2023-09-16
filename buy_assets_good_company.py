import time

from utils import clean_stock, get_cheap_asset
from utils.api_requests import get_latest_news_1_minute, sell_stock, limit_price_buy, info, RATE, MAX_QUANTITY


def buy_assets_from_news():
    latest_news = get_latest_news_1_minute()
    for news in latest_news:
        if news["rate"] > RATE:
            print("Есть подходящая новость!", end=" ")
            companies_affected = news["companiesAffected"]
            assets = clean_stock(sell_stock())
            buy_quantity = 0
            for asset in assets:
                if asset["ticker"] in companies_affected:
                    print("и у благоприятной компании есть акции")
                    price, quantity = get_cheap_asset(asset)
                    if quantity > MAX_QUANTITY:
                        quantity = MAX_QUANTITY - buy_quantity
                    buy_quantity += quantity
                    if buy_quantity <= MAX_QUANTITY:
                        limit_price_buy(asset["id"], price=price, quantity=quantity)
                        info()


while True:
    print("Проверка на наличие хороших акций")
    buy_assets_from_news()
    time.sleep(61)
