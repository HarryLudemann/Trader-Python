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
import Trader


class Example_Algorithm(Trader.Algorithm):
    """ Example Algorithm """

    def Init(self):
        self.Symbol = "TSLA"
        self.Name = "Tesla"
        self.StartDate = datetime.datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000

    def on_data(self):
        print(self.Symbol)



