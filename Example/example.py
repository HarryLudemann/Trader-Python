from trader import StockAlgorithm, run
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
        # print open item in data tuple
        #print(data[1]['open'])
        print(data)
        
    def stats(self):
        print(self.Name, 'Finished with', self.Cash)


test_algo = Algorithm()
test_algo.init()

run([test_algo])
