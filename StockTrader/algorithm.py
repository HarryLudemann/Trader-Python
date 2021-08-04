from abc import ABC, abstractmethod

class Algorithm(ABC):
    """ Abstract class to store algorithm infomation and functions """

    # Methods
    @abstractmethod
    def on_data(self):
        """ Abstract method to define whats happens on new data """
        pass

    # Properties
    @property
    @abstractmethod
    def Name(self, name):
        pass
        
    @property
    @abstractmethod
    def Symbol(self, symbol):
        pass
        
    @property
    @abstractmethod
    def StartDate(self, start_date):
        pass

    @property
    @abstractmethod
    def EndDate(self, end_date):
        pass
    
    @property
    @abstractmethod
    def Cash(self, cash):
        pass



if __name__ == '__main__':
    class TestAlgo(Algorithm):
        """ Test Algorithm """
        Name = "Test Algo"
        Symbol = "TEST"
        StartDate = "2018-01-01"
        EndDate = "2018-01-02"
        Cash = 100000

        def on_data(self):
            print(self.Symbol)


    TestAlgo().on_data()