# Modules
import os
import sys
import inspect

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


# abstract class
import trader


def test_stock_algorithm():
    """Checks the algorthm abstract class initializes properly returning value"""

    class TestAlgo(trader.StockAlgorithm):
        """ Test Algorithm that returns test symbol in on data"""
        def init(self):
            self.Symbol = "AAPL"
            self.Name = "Test Algo"
            self.StartDate = "2018-01-01"
            self.EndDate = "2018-01-02"
            self.Cash = 100000
            self.Data_Source = 'AlphaV'
            self.interval = "1m"

        def on_data(self):
            return self.Symbol
            
        def stats(self):
            print(self.Name, 'Finished with', self.Cash)

    algo = TestAlgo()
    algo.init()
    assert algo.on_data() == "AAPL"


def test_forex_algorithm():
    """Checks the algorthm abstract class initializes properly returning value"""

    class TestAlgo2(trader.ForexAlgorithm):
        """ Test Algorithm that returns test symbol in on data"""
        def init(self):
            self.To_Currency = "USD"
            self.From_Currency = "NZD"
            self.Name = "Test Algo"
            self.StartDate = "2018-01-01"
            self.EndDate = "2018-01-02"
            self.Cash = 100000
            self.Data_Source = 'AlphaV'
            self.interval = "1m"

        def on_data(self):
            return self.From_Currency
            
        def stats(self):
            print(self.Name, 'Finished with', self.Cash)

    algo = TestAlgo2()
    algo.init()
    assert algo.on_data() == "NZD"
