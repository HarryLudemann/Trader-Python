import pandas as pd   
import json
import requests

# Alpha Vantage API max 5 times per minute or 500 times a day


# retreive forex infomation methods:


# returns current price
def Get_Alpha_Forex_Exchange_Rate(ALPHA_VANTAGE_KEY, from_currency, to_currency):
    """
    Given from and to currency saves data to Live_data using alpha vantages CURRENCY_EXCHANGE_RATE api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&datatype=csv&from_currency={from_currency}$to_currency={to_currency}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   


def get_alpha_forex_fx_intraday(ALPHA_VANTAGE_KEY, from_currency, to_currency, interval):
    """
    Given from, to currency and interval(1min, 5min, 15min, 30min, 60min) saves data to Live_data using alpha vantages FX_INTRADAY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_INTRADAY&datatype=csv&from_symbol={from_currency}&to_symbol={to_currency}&interval={interval}&apikey=7PGWISTN90FB9RGV'
    return pd.read_csv(CSV_URL)


def get_alpha_forex_fx_daily(ALPHA_VANTAGE_KEY, from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_DAILY api
    """
    # CSV_URL = f'https://www.alphavantage.co/query?function=FX_DAILY&datatype=csv&from_symbol={from_symbol}$to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}'
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv'
    return pd.read_csv(CSV_URL)   


def get_alpha_forex_fx_weekly(ALPHA_VANTAGE_KEY, from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_WEEKLY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv'
    return pd.read_csv(CSV_URL)   


def get_alpha_forex_fx_monthly(ALPHA_VANTAGE_KEY, from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_MONTHLY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv'
    return pd.read_csv(CSV_URL)   

   


# retreive crypto infomation methods:




def fet_alpha_crypto_exchange_rate(ALPHA_VANTAGE_KEY, from_currency, to_currency):
    """
    Given given from and to currency returns current exchange rate using alpha vantages CURRENCY_EXCHANGE_RATE api
    returns 3 strings of Current Exchange Rate, bid price and ask price
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_KEY}'
    response = requests.get(CSV_URL)
    response.close()
    data = response.json()
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate'], data['Realtime Currency Exchange Rate']['8. Bid Price'], data['Realtime Currency Exchange Rate']['9. Ask Price']



def get_alpha_stock_intraday(ALPHA_VANTAGE_KEY, ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY api
    returns infomation from 1-2 months from 4:00am to 8:00pm Eastern Time for the US market
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&datatype=csv&interval={interval}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   




def get_alpha_stock_intraday_ext(ALPHA_VANTAGE_KEY, ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY_EXTENDED api
    trrailing 2 years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={ticker}&interval={interval}&slice=year1month1&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_daily(ALPHA_VANTAGE_KEY, ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_DAILY api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_daily_adj(ALPHA_VANTAGE_KEY, ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_DAILY_ADJUSTED api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_weekly(ALPHA_VANTAGE_KEY, ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_WEEKLY api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alpha_stock_weekly_adj(ALPHA_VANTAGE_KEY, ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_WEEKLY_ADJUSTED api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   


def get_alpha_stock_monthly(ALPHA_VANTAGE_KEY, ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_MONTHLY api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   


def get_alpha_stock_monthly_adj(ALPHA_VANTAGE_KEY, ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_MONTHLY_ADJUSTED api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    return pd.read_csv(CSV_URL)   



def get_alphav_forex(algorithm):  
    """passed algorithm calls appropraite api, returns df"""
    forex_df = pd.DataFrame()
    if algorithm.Interval == '1m':
        forex_df = get_alpha_forex_fx_intraday(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency, '1min')

    elif algorithm.Interval == '5m':
        forex_df = get_alpha_forex_fx_intraday(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency, '5min')

    elif algorithm.Interval == '15m':
        forex_df = get_alpha_forex_fx_intraday(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency, '15min')

    elif algorithm.Interval== '30m':
        forex_df = get_alpha_forex_fx_intraday(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency, '30min')

    elif algorithm.Interval== '60m':
        forex_df = get_alpha_forex_fx_intraday(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency, '60min')

    elif algorithm.Interval == '1d':
        forex_df = get_alpha_forex_fx_daily(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency)

    elif algorithm.Interval == '1w':
        forex_df = get_alpha_forex_fx_weekly(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency)

    elif algorithm.Interval == '1M':
        forex_df = get_alpha_forex_fx_monthly(algorithm.AlphaV_API, algorithm.from_currency, algorithm.to_currency)

    # rename timestamp column to Datetime
    forex_df.rename(columns={'timestamp':'Datetime'}, inplace=True)
    # use Datetime column as index
    forex_df.set_index('Datetime', inplace=True)
    return forex_df



# stock get methods

def get_alphav_stock(algorithm):
    """passed algorithm calls appropraite api, returns df"""
    if algorithm.Interval == '1m':
        stock_df = get_alpha_stock_intraday(algorithm.AlphaV_API, algorithm.ticker, '1min')
    elif algorithm.Interval == '5m':
        stock_df = get_alpha_stock_intraday(algorithm.AlphaV_API, algorithm.ticker, '5min')
    elif algorithm.Interval == '15m':
        stock_df = get_alpha_stock_intraday(algorithm.AlphaV_API, algorithm.ticker, '15min')
    elif algorithm.Interval== '30m':
        stock_df = get_alpha_stock_intraday(algorithm.AlphaV_API, algorithm.ticker, '30min')
    elif algorithm.Interval == '60m':
        stock_df = get_alpha_stock_intraday(algorithm.AlphaV_API, algorithm.ticker, '60min')
    # check if adjusted
    if algorithm.Adjusted:
        if algorithm.Interval == '1d':
            stock_df = get_alpha_stock_daily_adj(algorithm.AlphaV_API, algorithm.ticker)
        elif algorithm.Interval == '1w':
            stock_df = get_alpha_stock_weekly_adj(algorithm.AlphaV_API, algorithm.ticker)
        elif algorithm.Interval == '1m':
            stock_df = get_alpha_stock_monthly_adj(algorithm.AlphaV_API, '1M')
    else:
        if algorithm.Interval == '1d':
            stock_df = get_alpha_stock_daily(algorithm.AlphaV_API, algorithm.ticker)
        elif algorithm.Interval == '1w':
            stock_df = get_alpha_stock_weekly(algorithm.AlphaV_API, algorithm.ticker)
        elif algorithm.Interval == '1m':
            stock_df = get_alpha_stock_monthly(algorithm.AlphaV_API, '1M')
            
    # rename timestamp column to Datetime
    stock_df.rename(columns={'timestamp':'Datetime'}, inplace=True)
    # use Datetime column as index
    stock_df.set_index('Datetime', inplace=True)
    return stock_df

