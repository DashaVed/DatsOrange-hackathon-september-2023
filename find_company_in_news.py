import time

from utils import get_latest_news


last_news_date = get_latest_news()["date"]


def get_company_info_in_news(name):
    global last_news_date

    news = get_latest_news()
    if news["date"] == last_news_date:
        return

    last_news_date = news["date"]
    companies_affected = news["companiesAffected"]
    if name in companies_affected:
        print(f"Rate: {news['rate']} \n {news['text']}")
    else:
        print("The news doesn't content any information")


while True:
    get_company_info_in_news("NourishCraft Cafeteria")
    time.sleep(60)
