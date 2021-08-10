from trader import StockAlgorithm, backtest
from datetime import datetime

class Algorithm(StockAlgorithm):
    """ Example Algorithm to Run """

    def init(self):
        self.Active =True
        self.Backtest = True
        self.Name = "Example Algo"
        self.Symbol = "TSLA"
        self.StartDate = datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'yfinance'
        self.Adjusted = False
        self.Interval = "1m"

    def on_data(self, data):
        # print open item in data tuple
        print(data[1]['open'])

    def stats(self):
        print(self.Name, 'Finished with', self.Cash)

    def test(self):
        print(self.Name, 'Finished with', self.Cash)


# test_algo = Algorithm()
# test_algo.init()

# backtest(test_algo)


# function that takes two lists of ints x and y and returns a list of the numbers that arnt in both
def not_common(x, y):
    return [i for i in x + y if i in x and i not in y or i in y and i not in x]



print( not_common([13, 5, 6, 2, 5], [5, 2, 5, 13]) )
