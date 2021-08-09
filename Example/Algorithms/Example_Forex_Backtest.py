# modules
import os
import sys
import inspect
import datetime

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from trader import ForexAlgorithm

open_data = []
class Algorithm(ForexAlgorithm):
    """ Example Algorithm Backtesting """

    def Init(self):
        self.Active = True
        self.Name = "Example Forex Backtest"                   # Name of algorithm
        self.From_Currency = "USD"          # From Currency Ticker
        self.To_Currency = "NZD"            # To Current Ticker
        self.Cash = 100000                    # Cash allowed for algorithm to use
        self.Data_Source = "yfinance"            # Data Source for stock infomation (Check Data sources)
        self.Interval = "1d"               # Interval for data eg 1m, 5m, 1d, 1m
        self.StartDate = '2020-06-01'
        self.EndDate = '2021-06-01'
        self.Save_Data = True           # Wether to save the infomation collected for algorithm  - Default False
        self.Back_Test = True            # Wether to the strategy is to back test or to run  - Default False

    def on_data(self, data):
        # print open item in data tuple
        open_data.append(data[1]['open'])

    def stats(self):
        print(f'{self.Name} Finished with {str( len(open_data) )} lines of data')

