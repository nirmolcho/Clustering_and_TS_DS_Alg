import yfinance as yf
import pandas as pd
import time
import requests
import os

API_KEY = 'key'


def get_scraperapi_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


from urllib.parse import urlencode


def patched_get(url, *args, **kwargs):
    scraperapi_url = get_scraperapi_url(url)
    return original_get(scraperapi_url, *args, **kwargs)


original_get = requests.get  # Save the original get method
requests.get = patched_get  # Patch the get method


# Filtering function for annual data:
def filter_annual_data(df):
    df['Date'] = pd.to_datetime(df.index)
    return df[(df['Date'].dt.year >= 2020) & (df['Date'].dt.year <= 2023)]


# Filtering function for quarterly data:
def filter_quarterly_data(df):
    df['Date'] = pd.to_datetime(df.index)
    return df[(df['Date'].dt.year >= 2020) & (df['Date'].dt.year <= 2023)]


def fetch_financial_data(ticker_name):
    ticker = yf.Ticker(ticker_name)

    statements = {
        'income_stmt': filter_annual_data(ticker.income_stmt.T),
        'quarterly_income_stmt': filter_quarterly_data(ticker.quarterly_income_stmt.T),
        'balance_sheet': filter_annual_data(ticker.balance_sheet.T),
        'quarterly_balance_sheet': filter_quarterly_data(ticker.quarterly_balance_sheet.T),
        'cashflow': filter_annual_data(ticker.cashflow.T),
        'quarterly_cashflow': filter_quarterly_data(ticker.quarterly_cashflow.T),
    }

    for stmt_type, stmt in statements.items():
        time.sleep(1)
        stmt['Ticker'] = ticker_name
        time.sleep(1)

    return pd.concat(statements.values(), axis=0)


df = pd.read_csv("final_s&p500_df.csv")
df['Date'] = pd.to_datetime(df['Date'])
df1 = df.sample(10)

unique_tickers_dates = df1[['Ticker', 'Date']].drop_duplicates().values

dfs = []
for ticker_name, date in unique_tickers_dates:
    dfs.append(fetch_financial_data(ticker_name))
    time.sleep(1)

financial_data = pd.concat(dfs, axis=0)

merged_df = pd.merge(df1, financial_data, on=['Ticker', 'Date'], how='left')

merged_df.info()
