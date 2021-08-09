# Modules
import os           # for file operations
from datetime import datetime # get current date
#import time         # for sleep - scheduler

# Custom Modules
from trader import trade

# loading algorithms from file
import sys
from os import listdir
from os.path import isfile, join


def get_algorithms():
    """ returns list load of all classes in algorithms folder """
    algorithms = [] 
    # get list of python files NAMES(without.py) in Algorithms directory
    files = [f[:-3] for f in listdir('Algorithms') if  f.endswith('.py') and isfile(join('Algorithms', f))]
    sys.path.insert(0, 'Algorithms')        # move path into Algorithms directory
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


# load tickers
with open('tickers.txt', 'r') as tickers:
    tickers = tickers.read()
    tickers = tickers.split('\n')

# Create storage folders to store live data if don't exists
if not os.path.exists('Live-Data'):             os.makedirs('Live-Data')                      
if not os.path.exists('Live-Data/Stock'):       os.makedirs('Live-Data/Stock')                      
if not os.path.exists('Live-Data/Forex'):       os.makedirs('Live-Data/Forex')                      
if not os.path.exists('Live-Data/Crypto'):      os.makedirs('Live-Data')                      
if not os.path.exists('Live-Data/Algorithms'):  os.makedirs('Live-Data')     

Algorithms = get_algorithms()  # list of all Algorithm Objects
Backtest_Algorithms = [x for x in Algorithms if x.Active and x.Back_Test]   # list of Back Test Algorithms

print(f"\nStarting Backtesting {str( len(Backtest_Algorithms) )}\n")
for algorithm in Backtest_Algorithms:
    trade.back_test(algorithm)
    algorithm.stats()
print(f"\nBacktesting Finished\n")

# Run_Algorithms = [x for x in Algorithms if x.Active and x.Back_Test == False] # Run Algorithms  
# run method - loops while there is a active method
# print("Running Active Methods:")
# START_TIME = time.time()    # used for scheduler
# while(Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE) != []):
#     for algorithm in Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE):
#         Trader.Run(algorithm)

#     break # for testing only run once
#     time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))  # sleep for time until next minute from start of loop