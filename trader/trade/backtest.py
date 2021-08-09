# modules
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from trader import data


def back_test(algorithm):
    """ Method to backtest given algorithm object, gets data and passes each row to on_data method """
    if hasattr(algorithm, 'Symbol'):                # if algorithm is stock algo
        if algorithm.Data_Source == 'AlphaV':       # if using Alpha Vantage
            df = data.get_alphav_Stock(algorithm.Symbol, interval=algorithm.Interval, Adjusted=algorithm.Adjusted)
        elif algorithm.Data_Source == 'YFinance':   # if using YFinance 
            df = data.get_yfinance_stock(algorithm.Symbol, algorithm.StartDate, algorithm.EndDate, algorithm.Interval)
        if algorithm.Save_Data:                    
            # save dataframe to new csv file

            df.to_csv('Live-Data/Algorithms/' + algorithm.Name + '.csv')
            df.to_csv('Live-Data/Stock/' + algorithm.Symbol + '_'+ algorithm.Interval + '.csv')

    elif hasattr(algorithm, 'From_Currency'):       # if algorithm is forex method
        if algorithm.Data_Source == 'AlphaV':       # if using Alpha Vantage
            df = data.Get_alphav_forex(algorithm.From_Currency, algorithm.To_Currency, interval=algorithm.Interval)
        elif algorithm.Data_Source == 'YFinance':   # if using YFinance 
            df = data.get_yfinance_forex(algorithm.To_Currency, algorithm.From_Currency, algorithm.Interval, algorithm.StartDate, algorithm.EndDate)
        if algorithm.Save_Data: 
            df.to_csv('Live-Data/Algorithms/' + algorithm.Name + '.csv')
            df.to_csv('Live-Data/Forex/' + algorithm.From_Currency + '_' + algorithm.To_Currency + '_'+ algorithm.Interval + '.csv')
        
    start_date = df.index[0]   
    end_date = df.index[-1]

    print(f'Back Testing: {algorithm.Name}: {start_date} to, {end_date} interval: {algorithm.Interval}')

    for stock in df.iterrows():
        algorithm.on_data(stock)

    print(f'Finished: {algorithm.Name}: {start_date} to, {end_date} interval: {algorithm.Interval}')