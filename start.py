# Modules
import os           # for file operations
import time         # for sleep - scheduler
import datetime     # get current date

# Custom Modules
from StockTrader import Helper
from StockTrader import Data

# Initialize 
GET_MONTHS = 1                                                # Number of months to get historical daily data for
START_TIME = time.time()
TICKERS = Helper.Get_Tickers()                                # Load tickers from tickers.txt into list
START_DATE, END_DATE = Helper.Get_Dates(Months=GET_MONTHS)    # Get end date(current) and start date(-Get Months) for daily data

if not os.path.exists('Live-Data'):                           # Create folder to store live data if doesn't exists
    os.makedirs('Live-Data')
    os.makedirs('Live-Data/Stock')

Data.Create_Yfinance_Data(TICKERS, START_DATE, END_DATE)      # Create YFinance Data

StockAlgorithms = Helper.Load_Algorithms()                    # list of Algorithm Objects from Algorithms dir

# while loop that runs once a minute
time.sleep(60)                                                # wait 60 seconds before first update
DATA_DATE = END_DATE                                          # Set date to signal if daily data needs updating 
while True:
    # Update Minute Data
    Data.Update_Yfinance_Minute(TICKERS)                      # Update minute data for yfinance
    print("Minute Data Updated")


    # Check if next day, update daily data
    date = datetime.datetime.now().strftime("%Y-%m-%d")       # get current date
    if date != DATA_DATE:                                     # if date is different from data date update daily data
        Data.Update_Yfinance_Daily(TICKERS)                   # Update daily data for yfinance
        print("Daily Data Updated")


    # On new data send to all algorthms on_data() function


    time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))  # sleep for time until next minute from start of loop