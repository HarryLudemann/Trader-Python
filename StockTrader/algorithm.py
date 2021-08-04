from abc import ABC, abstractmethod

class Algorithm(ABC):
    """ Abstract class to store algorithm infomation and functions """
    def __init__(self, name, symbol, start_date, end_date):
        self.name = name
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    @abstractmethod
    def on_data(self):
        """ Abstract method to define whats happens on new data """
        pass



if __name__ == '__main__':
    
    class TestAlgo(Algorithm):
        """ Test Algorithm """
        def on_data(self):
            print("Test Algorithm")


    TestAlgo(name="Test", symbol="TEST", start_date="2018-01-01", end_date="2018-01-02").on_data()