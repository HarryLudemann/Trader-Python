# Modules
import os           # for file operations
import time         # for sleep - scheduler
from datetime import datetime     # get current date
from pytz import timezone   # timezones

# Custom Modules
from StockTrader import Helper
from StockTrader import Data
from StockTrader import Trader


Using_Free_Alpha_Vantage = True         # to signal rate limiting to prevent passing limits


START_DATE = datetime.now().strftime("%Y-%m-%d")  
START_TIME = time.time()    # used for scheduler
EST_TIME = datetime.now( timezone('EST') ).strftime("%H:%M:%S")    # get us eastern time
TICKERS = Helper.Get_Tickers()  


if not os.path.exists('Live-Data'):                           # Create folder to store live data if doesn't exists
    os.makedirs('Live-Data')
    os.makedirs('Live-Data/Stock')
    os.makedirs('Live-Data/Forex')
    os.makedirs('Live-Data/Crypto')
    os.makedirs('Live-Data/Algrithms')


Algorithms = Helper.Load_Algorithms()                    # list of Algorithm Objects from Algorithms dir
Algorithms = [x for x in Algorithms if x.Active]         # remove algorithms where active = false

# backtest methods where start and end date are before current date
Backtest_Algorithms = Helper.Load_Inactive_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE) # list inactive algo obj
print(f"\nStarting Backtesting\n")
for algorithm in Backtest_Algorithms:
    Trader.BackTest(algorithm)
    algorithm.stats()
print(f"\nBacktesting Finished\n")


# run method - loops while there is a active method
# print("Running Active Methods:")
# while(Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE) != []):
#     for algorithm in Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE):
#         Trader.Run(algorithm)

#     break # for testing only run once
#     time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))  # sleep for time until next minute from start of loop