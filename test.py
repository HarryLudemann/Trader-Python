from trader import StockAlgorithm, run, backtest
from datetime import datetime

open_data = []

class Algorithm(StockAlgorithm):
    """ Example Algorithm to Run """

    def init(self):
        self.Active =True
        self.Name = "Example Algo"
        self.Symbol = "TSLA"
        self.StartDate = datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'alphav'
        self.API_KEY = '7PGWISTN90FB9RGV'
        self.Adjusted = False
        self.Interval = "1m"

    def on_data(self, data):
        open_data.append(data)
        
    def stats(self):
        print(self.Name, 'Finished with', self.Cash)


test_algo = Algorithm()
test_algo.init()

backtest([test_algo])
run([test_algo])

