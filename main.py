import requests
from twilio.rest import Client

STOCK = "NVDA"  # the stock name of the company
COMPANY_NAME = "NVIDIA Corp"  # the name of the company
STOCK_Endpoint = "https://www.alphavantage.co/query"
stock_api_key = "stock api key"
NEWS_Endpoint = "https://newsapi.org/v2/everything"
news_api_key = "your news api key"
account_sid = "your twilio account sid"
auth_token = "your twilio auth sid"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}
news_parameters = {"q": COMPANY_NAME, "sortBy": "popularity", "apiKey": news_api_key}


response = requests.get(STOCK_Endpoint, params=stock_parameters)
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
difference = abs(
    float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
if abs(diff_percent) > 3:
    news_response = requests.get(NEWS_Endpoint, params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [
        f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{COMPANY_NAME}\n{article}",
            from_="Your twilio phone number",
            to="Your phone number",
        )
        print(message.status)
