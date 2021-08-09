import yfinance as yf
import pandas as pd
import os




def get_yfinance_date(interval, tickers, start_date, end_date):
    """
    Gets stock data from Yahoo Finance using start and end date
    Better for getting large amounts of data as 1m data is limited to 7 day period
    :param intervel eg 1d,start and end date in yy-mm-dd format and ticker:
    :return pandas dataFrame:
    """

    return yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = tickers,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        # period = "ytd",
        start = start_date,
        end = end_date,

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = interval,

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )




def get_yfinance_period(interval, tickers, period):
    """
    get data from yfinance using set periods
    better for getting 1m data using 7 day periods 
    :param intervel eg 1d, period eg 5d and ticker:
    :return pandas dataFrame:
    """

    return yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = tickers,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = period,

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = interval,

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )


def clean_yfinance_df(tickers, dataframe):
    """
    currently unused
    clean up given dataframe consisting of muiltple tickers to return list of dataframes
    :return list of pandas dataFrame:
    """
    option = ['Open', 'High', 'Low', 'Close', 'Volume']
    dataframe_list = []         # list of cleaned dataframes
    for ticker in tickers:
        df = pd.DataFrame()
        df['Open'] = dataframe[ticker][:10]     # add column to df

        for i in range(1,5):
            df[ option[i] ] = dataframe[ticker + f".{i}"][:10]   # add column to df

        # remove first 2 rows in df
        df = df.iloc[2:]
        
        df = df.astype(float)   # make all entries floats
        df['Date'] = dataframe.iloc[:,0]    # add date column

        dataframe_list.append(df)
    
    return dataframe_list

    
def get_yfinance_stock(ticker, start_date, end_date, interval):  
    """passed ticker, interval and adjusted calls appropraite api, returns df"""
    if interval == '1m':
        stock_df = get_yfinance_period(interval, [ticker], '7d')
    elif interval == '5m':
        stock_df = get_yfinance_period(interval, [ticker], '7d')
    elif interval == '15m':
        stock_df = get_yfinance_period(interval, [ticker], '7d')
    elif start_date == None or end_date == None:
        stock_df = get_yfinance_period(interval, [ticker], '7d')
    elif interval== '30m':
        stock_df = get_yfinance_date(interval, [ticker], start_date, end_date)
    elif interval == '60m':
        stock_df = get_yfinance_date(interval, [ticker], start_date, end_date)
    elif interval == '1d':
        stock_df = get_yfinance_date(interval, [ticker], start_date, end_date)
    elif interval == '1w':
        stock_df = get_yfinance_date('1wk', [ticker], start_date, end_date)
    elif interval == '1m':
        stock_df = get_yfinance_date('1mo', [ticker], start_date, end_date)

    # rename column names
    stock_df.columns = ['open', 'high', 'low', 'close', 'volume']
    return stock_df



def get_yfinance_forex(to_currency, from_currency, interval, start_date, end_date):  
    """passed ticker, interval and adjusted calls appropraite api, returns df"""
    ticker = f"{from_currency}{to_currency}=X"
    forex_df = pd.DataFrame()
    if interval == '1m':
        forex_df = get_yfinance_period(interval, ticker, '7d')
    elif interval == '5m':
        forex_df = get_yfinance_period(interval, ticker, '7d')
    elif interval == '15m':
        forex_df = get_yfinance_period(interval, ticker, '7d')
    elif start_date == None or end_date == None:
        forex_df = get_yfinance_period(interval, ticker, '7d')
    elif interval== '30m':
        forex_df = get_yfinance_date(interval, ticker, start_date, end_date)
    elif interval == '60m':
        forex_df = get_yfinance_date(interval, ticker, start_date, end_date)
    elif interval == '1d':
        forex_df = get_yfinance_date(interval,ticker, start_date, end_date)
    elif interval == '1w':
        forex_df = get_yfinance_date('1wk', ticker, start_date, end_date)
    elif interval == '1m':
        forex_df = get_yfinance_date('1mo',ticker, start_date, end_date)

    # rename column names
    forex_df.columns = ['open', 'high', 'low', 'close', 'volume']
    return forex_df