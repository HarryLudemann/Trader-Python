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




if __name__ == '__main__':
    # Get_Alpha_Stock_Intraday(ticker='AAPL', interval='5min')
    # Get_Alpha_Stock_Intraday_Ext(ticker='AAPL', interval='15min')
    # Get_Alpha_Stock_Daily(ticker='AAPL')
    # Get_Alpha_Stock_Daily_Adj(ticker='AAPL')
    # Get_Alpha_Stock_Weekly(ticker='AAPL')
    # Get_Alpha_Stock_Weekly_Adj(ticker='AAPL')
    Get_Alpha_Stock_Monthly(ticker='AAPL')
    Get_Alpha_Stock_Monthly_Adj(ticker='AAPL')