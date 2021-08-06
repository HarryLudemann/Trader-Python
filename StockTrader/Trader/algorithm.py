from abc import ABC, abstractmethod

class Algorithm(ABC):
    """ Abstract class to store algorithm infomation and functions """
    Name = ""                   # Name of algorithm
    Symbol = ""                 # Stock Ticker
    StartDate = None            # Start Date for algorithm (Some Datasources don't use)
    EndDate = None              # End Date for algorithm (Some Datasources don't use)
    Cash = 0                    # Cash allowed for algorithm to use
    Data_Source = ""            # Data Source for stock infomation (Check Data sources)
    Adjusted = False            # Wether to use Adjusted data (Some Datasources don't use)  - Default False
    Interval = ""               # Interval for data eg 1m, 5m, 1d, 1m
    Save_Data = False           # Wether to save the infomation collected for algorithm  - Default False
    Back_Test = False           # Wether to the strategy is to back test or to run  - Default False

    # Setter
    def setName(self, name):
        self.Name = name
    def setSymbol(self, symbol):
        self.Symbol = symbol
    def setStartDate(self, startDate):
        self.StartDate = startDate
    def setEndDate(self, endDate):
        self.EndDate = endDate
    def setCash(self, cash):
        self.Cash = cash
    def setData_Source(self, data_source):
        self.Data_Source = data_source
    def setInterval(self, interval):
        self.Interval = interval

    # Methods
    @abstractmethod
    def Init(self):
        """ Abstract method to define fields at creation """
        pass

    @abstractmethod
    def on_data(self, data):
        """ Abstract method to define what happens on new data, given tuple of data (timestrap, ohlc and volume) """
        pass





if __name__ == '__main__':
    class TestAlgo(Algorithm):
        """ Test Algorithm """

        def Init(self):
            self.Symbol = "AAPL"
            self.Name = "Test Algo"
            self.StartDate = "2018-01-01"
            self.EndDate = "2018-01-02"
            self.Cash = 100000
            self.Data_Source = 'AlphaV'
            self.Adjusted = False
            self.Interval = "1min"

        def on_data(self):
            print(self.Symbol)


    test_algo = TestAlgo()
    test_algo.Init()
    test_algo.on_data()