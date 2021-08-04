from abc import ABC, abstractmethod

class Algorithm(ABC):
    """ Abstract class to store algorithm infomation and functions """
    Name = ""
    Symbol = ""
    StartDate = ""
    EndDate = ""
    Cash = 0

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


    # Methods
    @abstractmethod
    def Init(self):
        """ Abstract method to define fields at creation """
        pass

    @abstractmethod
    def on_data(self):
        """ Abstract method to define what happens on new data """
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

        def on_data(self):
            print(self.Symbol)


    test_algo = TestAlgo()
    test_algo.Init()
    test_algo.on_data()