from decouple import config         # Getting .env variable
import requests                     # getting api infomation
import pandas as pd            
import json

# Alpha Vantage API max 5 times per minute or 500 times a day


def Get_Alpha_Stock_Intraday(ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY api
    returns infomation from 1-2 months from 4:00am to 8:00pm Eastern Time for the US market
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file

    # fetch data from Alpha Vantage
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&datatype=csv&interval={interval}&apikey={ALPHA_VANTAGE_KEY}'
    
    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SIntra{ticker}_{interval}.csv', index=False)




def Get_Alpha_Stock_Intraday_Ext(ticker, interval):
    """
    Given Ticker and interval saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY_Extended api
    trrailing 2 years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file

    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={ticker}&interval={interval}&slice=year1month1&apikey={ALPHA_VANTAGE_KEY}'

    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SIntraExtended_{ticker}_{interval}.csv', index=False)



def Get_Alpha_Stock_Daily(ticker):
    """
    Given Ticker saves data to Live_data using alpha vantages TIME_SERIES_Daily api
    covering 20+ years
    """
    ALPHA_VANTAGE_KEY = config('ALPHA_VANTAGE_KEY') # import Alpha Vantage Key from .env file
    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&slice=year1month1&apikey={ALPHA_VANTAGE_KEY}'

    df = pd.read_csv(CSV_URL)   
    df.to_csv(f'Live-Data/Stock/AlphaV_SDaily_{ticker}.csv', index=False)




if __name__ == '__main__':
    #Get_Alpha_Stock_Intraday(ticker='AAPL', interval='5min')
    #Get_Alpha_Stock_Intraday_Ext(ticker='AAPL', interval='15min')
    Get_Alpha_Stock_Daily(ticker='AAPL', interval='15min')