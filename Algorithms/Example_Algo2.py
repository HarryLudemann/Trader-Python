# modules
import os
import sys
import inspect

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

# custom modules
from StockTrader import Trader

class StockAlgorithm(Trader.Algorithm):
    """ Example Algorithm Backtesting """

    def Init(self):
        self.Name = "Example Stock Strategy2"
        self.Symbol = "AMZN"
        self.StartDate = '06/01/2020' # current time
        self.EndDate = '06/01/2021' # current time
        self.Cash = 100000
        self.Data_Source = 'YFinance'
        self.Adjusted = False
        self.Interval = "1m"
        self.Save_Data = True

    def on_data(self, data):
        # print open item in data tuple
        print(data[1]['Open'])



