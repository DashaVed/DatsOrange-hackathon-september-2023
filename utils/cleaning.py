from .api_requests import info, PRICE_TO_BUY


def get_now_oranges():
    data = info()
    for asset in data["assets"]:
        if asset["id"] == 1:
            return asset["quantity"]


def clean_stock(stock_data):
    clean_data = []
    for asset in stock_data:
        for bid in asset["bids"]:
            if bid.get("price", PRICE_TO_BUY) < PRICE_TO_BUY:
                data = {
                    "id": asset["id"],
                    "ticker": asset["ticker"],
                    "bids": asset["bids"]
                }
                clean_data.append(data)
                break
    return clean_data


def get_cheap_asset(asset):
    min_price = PRICE_TO_BUY
    quantity = 0
    for bid in asset["bids"]:
        if bid["price"] < min_price:
            min_price = bid["price"]
            quantity = bid["quantity"]
    return min_price, quantity
