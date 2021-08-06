# modules
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from StockTrader import Data


def BackTest(algorithm):
    # get data from appropriate source
    if algorithm.Data_Source == 'AlphaV':   # if using Alpha Vantage
        stock_df = Data.Get_AlphaV_Stock(algorithm.Symbol, interval=algorithm.Interval, Adjusted=algorithm.Adjusted)
        start_date = stock_df['timestamp'].iloc[0]
        end_date = stock_df['timestamp'].iloc[-1]

        print('Backtesting:', algorithm.Symbol, ':', start_date, 'to', end_date, 'interval:', algorithm.Interval)
        # iterate over each stock and pass tuple to algorithms on_data method
        for stock in stock_df.iterrows():
            algorithm.on_data(stock)

        if algorithm.Save_Data:
            stock_df.to_csv('Live-Data/Stock/' + algorithm.Name.strip() + '.csv')
        print('Finished', algorithm.Name, algorithm.Symbol, ':', start_date, 'to', end_date, 'interval:', algorithm.Interval)


    elif algorithm.Data_Source == 'YFinance':   # if using YFinance 
        stock_df = Data.Get_YFinance_Stock(algorithm.Symbol, algorithm.StartDate, algorithm.EndDate, algorithm.Interval)
        if algorithm.Save_Data:
            stock_df.to_csv('Live-Data/Stock/' + algorithm.Name.strip() + '.csv')

        # get first and last value
        start_date = stock_df.index[0].strftime('%Y-%m-%d')
        end_date = stock_df.index[-1].strftime('%Y-%m-%d')

        print('Backtesting:', algorithm.Symbol, ':', start_date, 'to', end_date, 'interval:', algorithm.Interval)
        # iterate over each stock and pass tuple to algorithms on_data method
        for stock in stock_df.iterrows():
            algorithm.on_data(stock)

        print('Finished', algorithm.Name, algorithm.Symbol, ':', start_date, 'to', end_date, 'interval:', algorithm.Interval)
