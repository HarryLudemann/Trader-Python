# Modules
import os
import sys
import inspect

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


# Custom Modules
from StockTrader import Trader


def test_algorithm():
    """Checks the algorthm abstract class initializes properly returning value"""

    class TestAlgo(Trader.Algorithm):
        """ Test Algorithm that returns test symbol in on data"""
        def Init(self):
            self.Symbol = "AAPL"
            self.Name = "Test Algo"
            self.StartDate = "2018-01-01"
            self.EndDate = "2018-01-02"
            self.Cash = 100000

        def on_data(self):
            return self.Symbol

    algo = TestAlgo()
    algo.Init()
    assert algo.on_data() == "AAPL"
