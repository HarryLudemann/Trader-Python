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

# Initialize 

if not os.path.exists('Live-Data'):                           # Create folder to store live data if doesn't exists
    os.makedirs('Live-Data')
    os.makedirs('Live-Data/Stock')
    os.makedirs('Live-Data/Forex')
    os.makedirs('Live-Data/Crypto')

Algorithms = Helper.Load_Algorithms()                    # list of Algorithm Objects from Algorithms dir

# backtest methods
InActive_Algorithms = Helper.Loaf_Inactive_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE) # list inactive algo obj
print("Starting Backtesting:")
for algorithm in InActive_Algorithms:
    Trader.BackTest(algorithm)
print("Backtesting Finished")




# run method - loops while there is a active method
while(Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE) != []):
    break # for testing, fun loop once
    for algorithm in Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE):
        if algorithm.Data_Source == 'AlphaV':   # if using Alpha Vantage
            if EST_TIME >= '04:00:00' and EST_TIME <= '20:00:00':   # check if EST_TIME is within 4 am and 8 pm
                    print("Within Trading Times")


    break # for testing, fun loop once
    time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))  # sleep for time until next minute from start of loop




# run
# GET_MONTHS = 1                                                # Number of months to get historical daily data for
# START_DATE, END_DATE = Helper.Get_Dates(Months=GET_MONTHS)    # Get end date(current) and start date(-Get Months) for daily data

# # while loop that runs once a minute
# time.sleep(60)                                                # wait 60 seconds before first update
# DATA_DATE = END_DATE                                          # Set date to signal if daily data needs updating 
# while True:
#     # Update Minute Data
#     Data.Update_Yfinance_Minute(TICKERS)                      # Update minute data for yfinance
#     print("Minute Data Updated")

#     # Update 5 Minute Data

#     # Check if next day, update daily data
#     date = datetime.datetime.now().strftime("%Y-%m-%d")       # get current date
#     if date != DATA_DATE:                                     # if date is different from data date update daily data
#         Data.Update_Yfinance_Daily(TICKERS)                   # Update daily data for yfinance
#         print("Daily Data Updated")


#     # On new data send to all algorthms on_data() function


#     time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))  # sleep for time until next minute from start of loop