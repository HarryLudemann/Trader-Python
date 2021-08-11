# Modules
import os           # for file operations
import time 
import asyncio      
from abc import ABC, abstractmethod # abstract classes

# Custom Modules
from trader import data

path = os.getcwd().replace('\\','/')     # path script is running from

class Algorithm(ABC):
    """ Class with variables that all algorithms have"""
    Name = ""                   # Name of algorithm
    Interval = ""               # Interval for data eg 1m, 5m, 1d, 1m
    Backtest = False            # Wether to the strategy is to back test or to run  - Default False
    API_KEY = None              # Alpha Vantage API key
    Cash = 0                    # Cash allowed for algorithm to use
    StartDate = None            # Start Date for algorithm (Some Datasources don't use)
    EndDate = None              # End Date for algorithm (Some Datasources don't use)
    Data_Source = ""            # Data Source for stock infomation (Check Data sources)
    Adjusted = False            # Wether to use Adjusted data (Some Datasources don't use)  - Default False
    Active = True               # Signal wether to run/backtest
    Time = ""                   # not set by user - used for scheduling in run method

    def set_start_date(self, startDate):
        self.StartDate = startDate
    def set_end_date(self, endDate):
        self.EndDate = endDate
    def set_cash(self, cash):
        self.Cash = cash
    def set_data_source(self, data_source):
        self.Data_Source = data_source
    def set_interval(self, interval):
        self.Interval = interval
    def set_name(self, name):
        self.Name = name
    def set_active(self, active):
        self.Active = active
    def set_adjusted(self, adjusted):
        self.Adjusted = adjusted

    # Abstract Methods
    @abstractmethod
    def init(self):
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


class StockAlgorithm(Algorithm):
    """ Abstract class to store algorithm infomation and functions for stock algorithms """
    Symbol = ""                 # Stock Ticker

    # Setter
    def set_symbol(self, symbol):
        self.Symbol = symbol


class ForexAlgorithm(Algorithm):
    """ Abstract class to store algorithm infomation and functions for forex algorithms"""
    From_Currency = ""          # From Currency Ticker
    To_Currency = ""          # To Currency Ticker

    # Setter
    def set_to_currency(self, from_currency):
        self.From_Currency = from_currency
    def set_from_currency(self, to_currency):
        self.To_Currency = to_currency



async def async_backtest(algorithm):
    """" Async method to backtest given algorithm object, gets data and passes each row to on_data method - dont call"""
    if algorithm.Active == False: return
    print(f'Getting {algorithm.Name} data, from {algorithm.Data_Source}')
    if hasattr(algorithm, 'Symbol'):                # if algorithm is stock algo
        df = await getattr(data, f'get_{algorithm.Data_Source}_stock')(algorithm)

    elif hasattr(algorithm, 'From_Currency'):       # if algorithm is forex method
        df = await getattr(data, f'get_{algorithm.Data_Source}_forex')(algorithm)
        
    start_date = df.index[0]    # start date of data   
    end_date = df.index[-1]     # end date of data

    print(f'Back Testing: {algorithm.Name}: {start_date} to, {end_date} interval: {algorithm.Interval} Data-Source: {algorithm.Data_Source}')
    # need alternative, somewhat slow
    for i in range(len(df)):
        algorithm.on_data(df.iloc[i])
    print(f'Finished: {algorithm.Name}: {start_date} to, {end_date} interval: {algorithm.Interval} Data-Source: {algorithm.Data_Source}')
    algorithm.stats()


async def create_backtest_tasks():
    """ method for backtest to create async tasks of each algorithm"""
    # async create task for each item in list
    tasks = [asyncio.ensure_future(async_backtest(algo)) for algo in backtest_algorithms]
    # wait for all tasks to complete
    await asyncio.wait(tasks)


def backtest(algorithms):
    """ Backtest method passed list of algorithms, calls on data for methods"""
    global backtest_algorithms
    backtest_algorithms = algorithms
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        #loop.set_debug(1)
        loop.run_until_complete(create_backtest_tasks())
    except Exception as e:
        print(e)
    finally:
        loop.close()


async def async_run(algorithm):
    """ runs given algorithm object if interval time has passed - dont call (used for run method)"""
    # get algorithms interval in minutes
    if algorithm.Interval[-1] == 'm':
        if algorithm.Interval[0] == '1' and algorithm.Interval[1] == '5':   # 15 minute interval
            algo_interval_minutes = 15
        elif algorithm.Interval[0] == '1':                                  # 1 minute interval
            algo_interval_minutes = 1
        elif algorithm.Interval[0] == '5':                                  # 5 minute interval
            algo_interval_minutes = 5
        elif algorithm.Interval[0] == '3':                                  # 30 minute interval
            algo_interval_minutes = 30
        elif algorithm.Interval[0] == '6':                                  # 60 minute interval
            algo_interval_minutes = 60
    elif algorithm.Interval[-1] == 'd':                                     # 1 day interval
        algo_interval_minutes = 1440
    elif algorithm.Interval[-1] == 'w':                                     # 1 week interval
        algo_interval_minutes = 10080
    elif algorithm.Interval[-1] == 'm':                                     # 1 month interval
        algo_interval_minutes = 43200
    elif algorithm.Interval[-1] == 'y':                                     # 1 year interval
        algo_interval_minutes = 525600
    
    # if time to run algorithm
    if minutes_ran % algo_interval_minutes == 0:
        # get appropriate data
        if hasattr(algorithm, 'Symbol'):                # if algorithm is stock algo
            df = await getattr(data, f'get_{algorithm.Data_Source}_stock')(algorithm)

        elif hasattr(algorithm, 'From_Currency'):       # if algorithm is forex method
            df = await getattr(data, f'get_{algorithm.Data_Source}_forex')(algorithm)

        algorithm.on_data(df.iloc[-1]) # call on data with last row in df
        algorithm.stats()
    await asyncio.sleep(0)


async def create_run_tasks():
    """ Create of async_run method for all run algorithms"""
    tasks = [asyncio.ensure_future(async_run(algo)) for algo in run_algorithms]
    # wait for all tasks to complete
    await asyncio.wait(tasks)


def run(Algorithms):
    """ Pass list of objects runs objects, returns nothing"""
    # currently not setup to be updatable while running
    start_time = time.time()    # for scheduling getting rest of of minute
    global run_algorithms 
    run_algorithms = [x for x in Algorithms if x.Active] 
    global minutes_ran 
    minutes_ran = 0 
    while True:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop = asyncio.get_event_loop()
            #loop.set_debug(1)
            loop.run_until_complete(create_run_tasks())
        except Exception as e:
            print(e)
        finally:
            loop.close()

        # wait for remainder of minute
        time.sleep(60.0 - ((time.time() - start_time) % 60.0))
        minutes_ran += 1