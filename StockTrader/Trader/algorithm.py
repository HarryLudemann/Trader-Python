from abc import ABC, abstractmethod

class Algorithm(ABC):
    """ Abstract class to store algorithm infomation and functions """
    Name = ""
    Symbol = ""
    StartDate = ""
    EndDate = None
    Cash = 0
    Data_Source = ""
    Adjusted = False
    Interval = ""

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