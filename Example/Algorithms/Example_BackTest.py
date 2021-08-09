# modules
import os
import sys
import inspect
import datetime

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from trader import StockAlgorithm


open_data = []
class Algorithm(StockAlgorithm):
    """ Example Algorithm Backtesting """

    def Init(self):
        self.Active = True
        self.Back_Test = True
        self.Name = "Example BackTest"
        self.Symbol = "GOOG"
        self.StartDate = '2020-06-01' # current time
        self.EndDate = '2021-06-01' # current time
        self.Cash = 100000
        self.Data_Source = 'yfinance'
        self.Adjusted = False
        self.Interval = "1m"
        self.Save_Data = True

    def on_data(self, data):
        # print open item in data tuple
        open_data.append(data[1]['open'])

    def stats(self):
        print(f'{self.Name} Finished with {str( len(open_data) )} lines of data')

