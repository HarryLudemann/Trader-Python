# modules
import os
import sys
import inspect
import datetime

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

# custom modules
from trader import trade

class Algorithm(trade.StockAlgorithm):
    """ Example Algorithm to Run """

    def Init(self):
        self.Active =False
        self.Name = "Example Algo"
        self.Symbol = "TSLA"
        self.StartDate = datetime.datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'AlphaV'
        self.Adjusted = False
        self.Interval = "1m"
        self.Save_Data = True

    def on_data(self, data):
        # print open item in data tuple
        print(data[1]['open'])

    def stats(self):
        print(self.Name, 'Finished with', self.Cash)



