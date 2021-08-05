# Modules
from Algorithms.Example_Algo import StockAlgorithm
import os           # for file operations
import time         # for sleep - scheduler
import datetime     # get current date

# Custom Modules
from StockTrader import Helper
from StockTrader import Data

# Initialize 
GET_MONTHS = 1                                                # Number of months to get historical daily data for
START_TIME = time.time()
TICKERS = Helper.get_tickers()                                # Load tickers from tickers.txt into list
START_DATE, END_DATE = Helper.get_dates(Months=GET_MONTHS)    # Get end date(current) and start date(-Get Months) for daily data

if not os.path.exists('Live-Data'):                           # Create folder to store live data if doesnt excists
    os.makedirs('Live-Data')

Data.Create_YFinance_Data(TICKERS, START_DATE, END_DATE)      # Create YFinance Data

StockAlgorithms = Helper.get_algorithms()                     # list of Algorithm Objects from Algorithms dir

# while loop that runs once a minute
DATA_DATE = END_DATE
while True:
    # Update Minute Data
    Data.Update_YFinance_Minute(TICKERS)
    print("Minute Data Updated")


    # Check if next day, update daily data
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    if date != DATA_DATE:               
        Data.Update_YFinance_Daily(TICKERS)
        print("Daily Data Updated")


    # On new data send to all algorthms on_data() function


    time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))  # sleep for time until next minute from start of loop