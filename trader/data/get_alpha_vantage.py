import pandas as pd   
import requests

# import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries
from alpha_vantage.async_support.foreignexchange import ForeignExchange



async def get_alphav_forex(algorithm):  
    """passed algorithm calls appropraite api, returns df"""
    fx = ForeignExchange(key=algorithm.API_KEY, output_format='pandas')

    forex_df = pd.DataFrame()
    if algorithm.Interval == '1m':
        forex_df, _ = await fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='1min', outputsize='compact')
    elif algorithm.Interval == '5m':
        forex_df, _ = await fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='5min', outputsize='compact')
    elif algorithm.Interval == '15m':
        forex_df, _ = await fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='15min', outputsize='compact')
    elif algorithm.Interval== '30m':
        forex_df, _ = await fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='30min', outputsize='compact')
    elif algorithm.Interval== '60m':
        forex_df, _ = await fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='60min', outputsize='compact')
    elif algorithm.Adjusted:
        if algorithm.Interval == '1d':
            forex_df, _ = await fx.get_currency_exchange_daily_adjusted(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
        elif algorithm.Interval == '1w':
            forex_df, _ = await fx.get_currency_exchange_weekly_adjusted(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
        elif algorithm.Interval == '1M':
            forex_df, _ = await fx.get_currency_exchange_monthly_adjusted(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
    else:
        if algorithm.Interval == '1d':
            forex_df, _ = await fx.get_currency_exchange_daily(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
        elif algorithm.Interval == '1w':
            forex_df, _ = await fx.get_currency_exchange_weekly(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
        elif algorithm.Interval == '1M':
            forex_df, _ = await fx.get_currency_exchange_monthly(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')

    fx.close()
    # rename timestamp column to Datetime
    forex_df.rename(columns={'date':'Datetime'}, inplace=True)
    forex_df.rename(columns={'1. open':'open'}, inplace=True)
    forex_df.rename(columns={'2. high':'high'}, inplace=True)
    forex_df.rename(columns={'3. low':'low'}, inplace=True)
    forex_df.rename(columns={'4. close':'close'}, inplace=True)
    forex_df.rename(columns={'5. volume':'volume'}, inplace=True)
    # use Datetime column as index
    # forex_df.set_index('Datetime', inplace=True)
    return forex_df



# stock get methods

async def get_alphav_stock(algorithm): 
    """passed algorithm calls appropraite api, returns df"""

    ts = TimeSeries(key=algorithm.API_KEY, output_format='pandas')
    if algorithm.Interval == '1m':
        stock_df, _ = await ts.get_intraday(symbol=algorithm.Symbol,interval='1min', outputsize='full')
    elif algorithm.Interval == '5m':
        stock_df, _ = await ts.get_intraday(symbol=algorithm.Symbol,interval='5min', outputsize='full')
    elif algorithm.Interval == '15m':
        stock_df, _ = await ts.get_intraday(symbol=algorithm.Symbol,interval='15min', outputsize='full')
    elif algorithm.Interval== '30m':
        stock_df, _ = await ts.get_intraday(symbol=algorithm.Symbol,interval='30min', outputsize='full')
    elif algorithm.Interval == '60m':
        stock_df, _ = await ts.get_intraday(symbol=algorithm.Symbol,interval='60min', outputsize='full')
    elif algorithm.Adjusted:
        if algorithm.Interval == '1d':
            stock_df, _ = await ts.get_daily_adjusted(symbol=algorithm.Symbol, outputsize='full')
        elif algorithm.Interval == '1w':
            stock_df, _ = await ts.get_weekly_adjusted(symbol=algorithm.Symbol, outputsize='full')
        elif algorithm.Interval == '1m':
            stock_df, _ = await ts.get_monthly_adjusted(symbol=algorithm.Symbol, outputsize='full')
    else:
        if algorithm.Interval == '1d':
            stock_df, _ = await ts.get_daily(symbol=algorithm.Symbol, outputsize='full')
        elif algorithm.Interval == '1w':
            stock_df, _ = await ts.get_weekly(symbol=algorithm.Symbol, outputsize='full')
        elif algorithm.Interval == '1m':
            stock_df, _ = await ts.get_monthly(symbol=algorithm.Symbol, outputsize='full')
    
    await ts.close()
            
    stock_df.rename(columns={'date':'Datetime'}, inplace=True)
    stock_df.rename(columns={'1. open':'open'}, inplace=True)
    stock_df.rename(columns={'2. high':'high'}, inplace=True)
    stock_df.rename(columns={'3. low':'low'}, inplace=True)
    stock_df.rename(columns={'4. close':'close'}, inplace=True)
    stock_df.rename(columns={'5. volume':'volume'}, inplace=True)
    # use Datetime column as index
    # stock_df.set_index('Datetime', inplace=True)
    return stock_df




# def get_alphav_forex(algorithm):  
#     """passed algorithm calls appropraite api, returns df"""
#     fx = ForeignExchange(key=algorithm.API_KEY, output_format='pandas')

#     forex_df = pd.DataFrame()
#     if algorithm.Interval == '1m':
#         forex_df, _ = fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='1min', outputsize='compact')
#     elif algorithm.Interval == '5m':
#         forex_df, _ = fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='5min', outputsize='compact')
#     elif algorithm.Interval == '15m':
#         forex_df, _ = fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='15min', outputsize='compact')
#     elif algorithm.Interval== '30m':
#         forex_df, _ = fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='30min', outputsize='compact')
#     elif algorithm.Interval== '60m':
#         forex_df, _ = fx.get_currency_exchange_intraday(algorithm.From_Currency, algorithm.To_Currency, interval='60min', outputsize='compact')
#     elif algorithm.Adjusted:
#         if algorithm.Interval == '1d':
#             forex_df, _ = fx.get_currency_exchange_daily_adjusted(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
#         elif algorithm.Interval == '1w':
#             forex_df, _ = fx.get_currency_exchange_weekly_adjusted(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
#         elif algorithm.Interval == '1M':
#             forex_df, _ = fx.get_currency_exchange_monthly_adjusted(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
#     else:
#         if algorithm.Interval == '1d':
#             forex_df, _ = fx.get_currency_exchange_daily(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
#         elif algorithm.Interval == '1w':
#             forex_df, _ = fx.get_currency_exchange_weekly(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')
#         elif algorithm.Interval == '1M':
#             forex_df, _ = fx.get_currency_exchange_monthly(algorithm.From_Currency, algorithm.To_Currency, outputsize='compact')


#     rename timestamp column to Datetime
#     forex_df.rename(columns={'date':'Datetime'}, inplace=True)
#     forex_df.rename(columns={'1. open':'open'}, inplace=True)
#     forex_df.rename(columns={'2. high':'high'}, inplace=True)
#     forex_df.rename(columns={'3. low':'low'}, inplace=True)
#     forex_df.rename(columns={'4. close':'close'}, inplace=True)
#     forex_df.rename(columns={'5. volume':'volume'}, inplace=True)
#     use Datetime column as index
#     forex_df.set_index('Datetime', inplace=True)
#     return forex_df



# stock get methods

# def get_alphav_stock(algorithm): 
#     """passed algorithm calls appropraite api, returns df"""

#     ts = TimeSeries(key=algorithm.API_KEY, output_format='pandas')
#     if algorithm.Interval == '1m':
#         stock_df, _ = ts.get_intraday(symbol=algorithm.Symbol,interval='1min', outputsize='full')
#     elif algorithm.Interval == '5m':
#         stock_df, _ = ts.get_intraday(symbol=algorithm.Symbol,interval='5min', outputsize='full')
#     elif algorithm.Interval == '15m':
#         stock_df, _ = ts.get_intraday(symbol=algorithm.Symbol,interval='15min', outputsize='full')
#     elif algorithm.Interval== '30m':
#         stock_df, _ = ts.get_intraday(symbol=algorithm.Symbol,interval='30min', outputsize='full')
#     elif algorithm.Interval == '60m':
#         stock_df, _ = ts.get_intraday(symbol=algorithm.Symbol,interval='60min', outputsize='full')
#     elif algorithm.Adjusted:
#         if algorithm.Interval == '1d':
#             stock_df, _ = ts.get_daily_adjusted(symbol=algorithm.Symbol, outputsize='full')
#         elif algorithm.Interval == '1w':
#             stock_df, _ = ts.get_weekly_adjusted(symbol=algorithm.Symbol, outputsize='full')
#         elif algorithm.Interval == '1m':
#             stock_df, _ = ts.get_monthly_adjusted(symbol=algorithm.Symbol, outputsize='full')
#     else:
#         if algorithm.Interval == '1d':
#             stock_df, _ = ts.get_daily(symbol=algorithm.Symbol, outputsize='full')
#         elif algorithm.Interval == '1w':
#             stock_df, _ = ts.get_weekly(symbol=algorithm.Symbol, outputsize='full')
#         elif algorithm.Interval == '1m':
#             stock_df, _ = ts.get_monthly(symbol=algorithm.Symbol, outputsize='full')
            
#     stock_df.rename(columns={'date':'Datetime'}, inplace=True)
#     stock_df.rename(columns={'1. open':'open'}, inplace=True)
#     stock_df.rename(columns={'2. high':'high'}, inplace=True)
#     stock_df.rename(columns={'3. low':'low'}, inplace=True)
#     stock_df.rename(columns={'4. close':'close'}, inplace=True)
#     stock_df.rename(columns={'5. volume':'volume'}, inplace=True)
#     use Datetime column as index
#     stock_df.set_index('Datetime', inplace=True)
#     return stock_df

