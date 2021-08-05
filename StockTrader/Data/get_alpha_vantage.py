from decouple import config         # Getting .env variable
import pandas as pd   

# Alpha Vantage API max 5 times per minute or 500 times a day

ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file

# retreive stocks infomation methods:


def Get_Alpha_Stock_Intraday(ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY api
    returns infomation from 1-2 months from 4:00am to 8:00pm Eastern Time for the US market
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&datatype=csv&interval={interval}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SIntra{ticker}_{interval}.csv', index=False)




def Get_Alpha_Stock_Intraday_Ext(ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY_Extended api
    trrailing 2 years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={ticker}&interval={interval}&slice=year1month1&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SIntraExtended_{ticker}_{interval}.csv', index=False)



def Get_Alpha_Stock_Daily(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_DAILY api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SDaily_{ticker}.csv', index=False)



def Get_Alpha_Stock_Daily_Adj(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_DAILY_ADJUSTED api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SDailyAdj_{ticker}.csv', index=False)



def Get_Alpha_Stock_Weekly(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_WEEKLY api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SWeekly_{ticker}.csv', index=False)



def Get_Alpha_Stock_Weekly_Adj(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_WEEKLY_ADJUSTED api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SWeeklyAdj_{ticker}.csv', index=False)


def Get_Alpha_Stock_Monthly(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_MONTHLY api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SMonthly_{ticker}.csv', index=False)


def Get_Alpha_Stock_Monthly_Adj(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_MONTHLY_ADJUSTED api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SMonthlyAdj_{ticker}.csv', index=False)


def Get_Alpha_Stock_Monthly_Adj(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_MONTHLY_ADJUSTED api
    covering 20+ years
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&datatype=csv&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SMonthlyAdj_{ticker}.csv', index=False)



# retreive forex infomation methods:


def Get_Alpha_Forex_Exchange_Rate(from_currency, to_currency):
    """
    Given from and to currency saves data to Live_data using alpha vantages CURRENCY_EXCHANGE_RATE api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&datatype=csv&from_currency={from_currency}$to_currency={to_currency}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Forex/AlphaV_FExchangeRate_{from_currency}_{to_currency}.csv', index=False)


def Get_Alpha_Forex_FX_Intraday(from_currency, to_currency, interval):
    """
    Given from, to currency and interval(1min, 5min, 15min, 30min) saves data to Live_data using alpha vantages FX_INTRADAY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_INTRADAY&datatype=csv&interval={interval}&from_symbol={from_currency}$to_symbol={to_currency}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Forex/AlphaV_FFXIntraday_{interval}_{from_currency}_{to_currency}.csv', index=False)


def Get_Alpha_Forex_Crypto_Intraday(symbol, market, interval):
    """
    Given symbol, market and interval(1min, 5min, 15min, 30min) saves data to Live_data using alpha vantages CRYPTO_INTRADAY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_INTRADAY&datatype=csv&interval={interval}&symbol={symbol}$market={market}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Forex/AlphaV_FCryptoIntra_{interval}_{market}_{symbol}.csv', index=False)



def Get_Alpha_Forex_FX_Daily(from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_DAILY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_DAILY&datatype=csv&from_symbol={from_symbol}$to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Forex/AlphaV_FFXDaily_{from_symbol}_{to_symbol}.csv', index=False)


def Get_Alpha_Forex_FX_Weekly(from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_WEEKLY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_WEEKLY&datatype=csv&from_symbol={from_symbol}$to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Forex/AlphaV_FFXWeekly_{from_symbol}_{to_symbol}.csv', index=False)


def Get_Alpha_Forex_FX_Monthly(from_symbol, to_symbol):
    """
    Given from and to symbol saves data to Live_data using alpha vantages FX_MONTHLY api
    """
    CSV_URL = f'https://www.alphavantage.co/query?function=FX_MONTHLY&datatype=csv&from_symbol={from_symbol}$to_symbol={to_symbol}&apikey={ALPHA_VANTAGE_KEY}'
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Forex/AlphaV_FFXMonthly_{from_symbol}_{to_symbol}.csv', index=False)


# retreive crypto infomation methods:



if __name__ == '__main__':
    Get_Alpha_Forex_FX_Weekly(from_symbol='ETH', to_symbol='USD')
