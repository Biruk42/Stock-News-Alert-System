# Stock-News-Alert-System
This project retrieves stock data and relevant news articles based on a specified company's stock symbol and sends alerts via SMS using Twilio.

## Prerequisites

Before running this program, ensure you have the following:

- Python 3.x installed
- Required Python libraries installed (requests, twilio)
- API keys from Alpha Vantage for stock data and News API for news articles
- Twilio account credentials (Account SID and Auth Token)
## Configuration

- `STOCK`: The stock symbol of the company you want to track.
- `COMPANY_NAME`: The name of the company.
- `STOCK_Endpoint`: Endpoint for retrieving stock data (e.g., Alpha Vantage API).
- `stock_api_key`: API key for accessing stock data.
- `NEWS_Endpoint`: Endpoint for retrieving news articles (e.g., News API).
- `news_api_key`: API key for accessing news articles.
- `account_sid`: Your Twilio account SID.
- `auth_token`: Your Twilio authentication token.
