from trader import StockAlgorithm, run, backtest
from datetime import datetime

class Algorithm(StockAlgorithm):
    """ Example Algorithm to Run """

    def init(self):
        self.Active =True
        self.Name = "Example Algo"
        self.Symbol = "TSLA"
        self.StartDate = datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'yfinance'
        self.Adjusted = False
        self.Interval = "1m"

    def on_data(self, data):
        print(data)
        
    def stats(self):
        print(self.Name, 'Finished with', self.Cash)


test_algo = Algorithm()
test_algo.init()

backtest([test_algo])

