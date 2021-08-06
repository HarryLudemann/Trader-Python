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


open_data = []

class StockAlgorithm(Trader.StockAlgorithm):
    """ Example Algorithm Backtesting """

    def Init(self):
        self.Back_Test = True
        self.Name = "Example Back Test"
        self.Symbol = "AMZN"
        self.StartDate = '2020-06-01' # current time
        self.EndDate = '2021-06-01' # current time
        self.Cash = 100000
        self.Data_Source = 'YFinance'
        self.Adjusted = False
        self.Interval = "1m"
        self.Save_Data = True

    def on_data(self, data):
        # print open item in data tuple
        open_data.append(data[1]['open'])
        print( len(open_data) )

    def stats(self):
        print(self.Name, 'Finished with', self.Cash)

