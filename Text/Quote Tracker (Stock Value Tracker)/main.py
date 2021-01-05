import requests
import json
import time
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()
API_KEY = os.getenv("API_KEY")
# YYYY/MM/DD format, (example: '2021-01-05')
currentDay = date.today().strftime('%Y-%m-%d')
key = API_KEY


def getCurrentStockPrice(ticker):
    try:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(
            ticker, key)
        response = requests.get(url)
        data = response.json()

        currentDayStockPriceInfo = data.get('Time Series (Daily)')[currentDay]
        currentStockPrice = currentDayStockPriceInfo['5. adjusted close']

        # print(currentDayStockPriceInfo)
        print(f"{ticker}'s current stock price is: {currentStockPrice}")
    except:
        print('Invalid company symbol!')


# 5 API requests per minute is the limit;
topCompanies = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA']

for company in topCompanies:
    getCurrentStockPrice(company)
