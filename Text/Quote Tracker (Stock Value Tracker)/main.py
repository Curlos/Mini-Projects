import requests
import json
import time
from dotenv import load_dotenv
import os
from datetime import date
from datetime import timedelta
from pprint import pprint

load_dotenv()
API_KEY = os.getenv("API_KEY")
key = API_KEY


def getCurrentStockPrice(ticker):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}'.format(
        ticker, key)
    try:
        response = requests.get(url)
        data = response.json()
        latestTimeUpdated = list(data.get('Time Series (5min)').keys())[0]

        currentStockPriceInfo = data.get('Time Series (5min)')[
            latestTimeUpdated]
        currentStockPrice = currentStockPriceInfo['4. close']
        print(f"{ticker}'s current stock price is: {currentStockPrice}")
    except:
        print('Request limit reached. Please run the program again in 1 minute.')


# 5 API requests per minute is the limit;
topCompanies = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA']

for company in topCompanies:
    getCurrentStockPrice(company)
