from decouple import config         # Getting .env variable
import pandas as pd   
import json
import requests

# Alpha Vantage API max 5 times per minute or 500 times a day


# retreive forex infomation methods:


# returns current price
def Get_Alpha_Forex_Exchange_Rate(from_currency, to_currency):
    """
    Given from and to currency saves data to Live_data using alpha vantages CURRENCY_EXCHANGE_RATE api
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&datatype=csv&from_currency={from_currency}$to_currency={to_currency}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   


def get_alpha_forex_fx_intraday(from_currency, to_currency, interval):
    """
    Given from, to currency and interval(1min, 5min, 15min, 30min, 60min) saves data to Live_data using alpha vantages FX_INTRADAY api
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_INTRADAY&datatype=csv&from_symbol={from_currency}&to_symbol={to_currency}&interval={interval}&apikey=7PGWISTN90FB9RGV'
    return pd.read_csv(CSV_URL)


def get_alpha_forex_fx_daily(from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_DAILY api
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    # CSV_URL = f'https://www.alphavantage.co/query?function=FX_DAILY&datatype=csv&from_symbol={from_symbol}$to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}'
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv'
    return pd.read_csv(CSV_URL)   


def get_alpha_forex_fx_weekly(from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_WEEKLY api
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    # CSV_URL = f'https://www.alphavantage.co/query?function=FX_WEEKLY&datatype=csv&from_symbol={from_symbol}$to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}'
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv'
    return pd.read_csv(CSV_URL)   


def get_alpha_forex_fx_monthly(from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_MONTHLY api
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv'
    return pd.read_csv(CSV_URL)   

   


# retreive crypto infomation methods:




def fet_alpha_crypto_exchange_rate(from_currency, to_currency):
    """
    Given given from and to currency returns current exchange rate using alpha vantages CURRENCY_EXCHANGE_RATE api
    returns 3 strings of Current Exchange Rate, bid price and ask price
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_KEY}'
    response = requests.get(CSV_URL)
    response.close()
    data = response.json()
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate'], data['Realtime Currency Exchange Rate']['8. Bid Price'], data['Realtime Currency Exchange Rate']['9. Ask Price']



def get_alpha_stock_intraday(ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY api
    returns infomation from 1-2 months from 4:00am to 8:00pm Eastern Time for the US market
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&datatype=csv&interval={interval}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   




def get_alpha_stock_intraday_ext(ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY_EXTENDED api
    trrailing 2 years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={ticker}&interval={interval}&slice=year1month1&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_daily(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_DAILY api
    covering 20+ years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_daily_adj(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_DAILY_ADJUSTED api
    covering 20+ years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_weekly(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_WEEKLY api
    covering 20+ years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_weekly_adj(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_WEEKLY_ADJUSTED api
    covering 20+ years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   


def get_alpha_stock_monthly(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_MONTHLY api
    covering 20+ years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   


def get_alpha_stock_monthly_adj(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_MONTHLY_ADJUSTED api
    covering 20+ years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alphav_forex(from_currency, to_currency, interval):  
    """passed ticker, interval and adjusted calls appropraite api, returns df"""
    forex_df = pd.DataFrame()
    if interval == '1m':
        forex_df = get_alpha_forex_fx_intraday(from_currency, to_currency, '1min')

    elif interval == '5m':
        forex_df = get_alpha_forex_fx_intraday(from_currency, to_currency, '5min')

    elif interval == '15m':
        forex_df = get_alpha_forex_fx_intraday(from_currency, to_currency, '15min')

    elif interval== '30m':
        forex_df = get_alpha_forex_fx_intraday(from_currency, to_currency, '30min')

    elif interval== '60m':
        forex_df = get_alpha_forex_fx_intraday(from_currency, to_currency, '60min')

    elif interval == '1d':
        forex_df = get_alpha_forex_fx_daily(from_currency, to_currency)

    elif interval == '1w':
        forex_df = get_alpha_forex_fx_weekly(from_currency, to_currency)

    elif interval == '1M':
        forex_df = get_alpha_forex_fx_monthly(from_currency, to_currency)

    # rename timestamp column to Datetime
    forex_df.rename(columns={'timestamp':'Datetime'}, inplace=True)
    # use Datetime column as index
    forex_df.set_index('Datetime', inplace=True)
    return forex_df



# stock get methods


def get_alphav_stock(ticker, interval=None, Adjusted=False):  
    """passed ticker, interval and adjusted calls appropraite api, returns df"""
    if interval == '1m':
        stock_df = get_alpha_stock_intraday(ticker, '1min')
    elif interval == '5m':
        stock_df = get_alpha_stock_intraday(ticker, '5min')
    elif interval == '15m':
        stock_df = get_alpha_stock_intraday(ticker, '15min')
    elif interval== '30m':
        stock_df = get_alpha_stock_intraday(ticker, '30min')
    elif interval == '60m':
        stock_df = get_alpha_stock_intraday(ticker, '60min')
    # check if adjusted
    if Adjusted:
        if interval == '1d':
            stock_df = get_alpha_stock_daily_adj(ticker)
        elif interval == '1w':
            stock_df = get_alpha_stock_weekly_adj(ticker)
        elif interval == '1m':
            stock_df = get_alpha_stock_monthly_adj('1M')
    else:
        if interval == '1d':
            stock_df = get_alpha_stock_daily(ticker)
        elif interval == '1w':
            stock_df = get_alpha_stock_weekly(ticker)
        elif interval == '1m':
            stock_df = get_alpha_stock_monthly('1M')
            
    # rename timestamp column to Datetime
    stock_df.rename(columns={'timestamp':'Datetime'}, inplace=True)
    # use Datetime column as index
    stock_df.set_index('Datetime', inplace=True)
    return stock_df
