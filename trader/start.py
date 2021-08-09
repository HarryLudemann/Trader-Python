# Modules
import os           # for file operations
from datetime import datetime # get current date
#import time         # for sleep - scheduler

# Custom Modules
from trader import data

# loading algorithms from file
import sys
from os import listdir
from os.path import isfile, join

# abstract classes
from abc import ABC, abstractmethod

path = os.getcwd().replace('\\','/')     # path script is running from

class StockAlgorithm(ABC):
    """ Abstract class to store algorithm infomation and functions for stock algorithms """
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

    @abstractmethod
    def stats(self):
        """ Abstract method to define what stats to return """
        pass




class ForexAlgorithm(ABC):
    """ Abstract class to store algorithm infomation and functions for forex algorithms"""
    Active = True               # Signal wether to run/backtest
    Name = ""                   # Name of algorithm
    From_Currency = ""          # From Currency Ticker
    To_Currency = ""          # To Currency Ticker
    StartDate = None            # Start Date for algorithm (Some Datasources don't use)
    EndDate = None              # End Date for algorithm (Some Datasources don't use)
    Cash = 0                    # Cash allowed for algorithm to use
    Data_Source = ""            # Data Source for stock infomation (Check Data sources)
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

    @abstractmethod
    def stats(self):
        """ Abstract method to define what stats to return """
        pass


def back_test(algorithm):
    """ Method to backtest given algorithm object, gets data and passes each row to on_data method """
    if hasattr(algorithm, 'Symbol'):                # if algorithm is stock algo
        df = getattr(data, f'get_{algorithm.Data_Source}_stock')(algorithm.Symbol, algorithm.StartDate, algorithm.EndDate, algorithm.Interval, algorithm.Adjusted)
        if algorithm.Save_Data:                     # if saving data
            df.to_csv(f'{path}/Live-Data/Algorithms/' + algorithm.Name + '.csv')
            df.to_csv(f'{path}/Live-Data/Stock/' + algorithm.Symbol + '_'+ algorithm.Interval + '.csv')

    elif hasattr(algorithm, 'From_Currency'):       # if algorithm is forex method
        df = getattr(data, f'get_{algorithm.Data_Source}_forex')(algorithm.To_Currency, algorithm.From_Currency, algorithm.Interval, algorithm.StartDate, algorithm.EndDate)
        if algorithm.Save_Data:                     # if saving data
            df.to_csv(f'{path}/Live-Data/Algorithms/' + algorithm.Name + '.csv')
            df.to_csv(f'{path}/Live-Data/Forex/' + algorithm.From_Currency + '_' + algorithm.To_Currency + '_'+ algorithm.Interval + '.csv')
        
    start_date = df.index[0]    # start date of data   
    end_date = df.index[-1]     # end date of data

    print(f'Back Testing: {algorithm.Name}: {start_date} to, {end_date} interval: {algorithm.Interval} Data-Source: {algorithm.Data_Source}')

    for stock in df.iterrows(): # for each row in data call on_data method in the algorithm obj
        algorithm.on_data(stock)

    print(f'Finished: {algorithm.Name}: {start_date} to, {end_date} interval: {algorithm.Interval} Data-Source: {algorithm.Data_Source}')


def get_algorithms():
    """ returns list load of all classes in algorithms folder """
    algorithms = [] 
    # get list of python files NAMES(without.py) in Algorithms directory
    files = [f[:-3] for f in listdir(f'{path}/Algorithms') if  f.endswith('.py') and isfile(join('Algorithms', f))]
    sys.path.insert(0, f'{path}/Algorithms')        # move path into Algorithms directory
    for file in files:                      # iterate over files
        file = __import__(file)             # import file
        algorithm_obj = file.Algorithm()    # create an instance of the class
        algorithm_obj.Init()                # Run Init method in class
        algorithms.append(algorithm_obj)    # add instance to list
    return algorithms                       # return list of instances


def get_active_algorithms(Algorithms):
    """ returns list of run classes from given list of active, not back test algorithms  """
     # get list of stocks where current date is within start and end date (optional)
    active_algorithms = []      
    current_date = datetime.now().strftime("%Y-%m-%d")  # current date
    for algorithm in Algorithms:
        algo_start = algorithm.StartDate
        algo_end = algorithm.EndDate
        if (algo_end != None):      
            if algo_start <= current_date and algo_end >= current_date:
                active_algorithms.append(algorithm)    
        else:
            if algo_start <= current_date:
                active_algorithms.append(algorithm)    
        
    return active_algorithms


def run():
    """ Main method to run functions """
    # load tickers
    with open('tickers.txt', 'r') as tickers:
        tickers = tickers.read()
        tickers = tickers.split('\n')   

    Algorithms = get_algorithms()  # list of all Algorithm Objects
    Backtest_Algorithms = [x for x in Algorithms if x.Active and x.Back_Test]   # list of Back Test Algorithms

    # Create storage folders to store live data if don't exists
    if not os.path.exists('Live-Data'):             os.makedirs('Live-Data')                      
    if not os.path.exists('Live-Data/Stock'):       os.makedirs('Live-Data/Stock')                      
    if not os.path.exists('Live-Data/Forex'):       os.makedirs('Live-Data/Forex')                      
    if not os.path.exists('Live-Data/Crypto'):      os.makedirs('Live-Data')                      
    if not os.path.exists('Live-Data/Algorithms'):  os.makedirs('Live-Data')  

    print("\nStarting Backtesting\n")
    for algorithm in Backtest_Algorithms:
        back_test(algorithm)
        algorithm.stats()
    print("\nBacktesting Finished\n")

    # Run_Algorithms = [x for x in Algorithms if x.Active and x.Back_Test == False] # Run Algorithms  
    # run method - loops while there is a active method
    # print("Running Active Methods:")
    # START_TIME = time.time()    # used for scheduler
    # while(Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE) != []):
    #     for algorithm in Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE):
    #         Trader.Run(algorithm)

    #     break # for testing only run once
    #     time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))  # sleep for time until next minute from start of loop

