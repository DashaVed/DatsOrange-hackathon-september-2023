import requests
from decouple import config


URL = "https://datsorange.devteam.games/"
TOKEN = config("TOKEN")
HEADERS = {"token": TOKEN, "Content-Type": "application/json"}

PRICE_TO_BUY = 300
PRICE_TO_SELL = 100
RATE = 30
MAX_QUANTITY = 10


def info():
    request = requests.get(f"{URL}/info", headers={"token": TOKEN})
    return request.json()


def sell_stock():
    request = requests.get(f"{URL}/sellStock", headers={"token": TOKEN})
    return request.json() if request.status_code == 200 else []


def limit_price_buy(symbol_id, price, quantity):
    request = requests.post(f"{URL}/LimitPriceBuy",
                            json={"symbolId": symbol_id, "price": price, "quantity": quantity},
                            headers=HEADERS)
    if request.status_code == 200:
        print(f"Акции компании с id {symbol_id} куплены в количестве {quantity} шт. по цене {price}")
    else:
        print(request.status_code)
    return


def limit_price_sell(symbol_id, price, quantity):
    request = requests.post(f"{URL}/LimitPriceSell",
                            json={"symbolId": symbol_id, "price": price, "quantity": quantity},
                            headers=HEADERS)
    if request.status_code == 200:
        print(f"Было выставлено на продажу {quantity} акций на {price} у компании c id={symbol_id}")
    else:
        print(request.status_code)
    return


def best_price_sell(symbol_id, quantity):
    request = requests.post(f"{URL}/BestPriceSell",
                            json={"symbolId": symbol_id, "quantity": quantity},
                            headers=HEADERS)
    print(request.status_code)
    return


def get_latest_news():
    request = requests.get(f"{URL}/news/LatestNews", headers={"token": TOKEN})
    return request.json() if request.status_code == 200 else None


def get_latest_news_1_minute():
    request = requests.get(f"{URL}/news/LatestNews1Minute", headers={"token": TOKEN})
    return request.json() if request.status_code == 200 else []
