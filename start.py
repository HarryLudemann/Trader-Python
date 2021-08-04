# Modules
import os           # for file operations
import time         # for sleep - scheduler

# Custom Modules
from StockTrader import Helper
from StockTrader import Data

# Initialize 
GET_MONTHS = 1                                                # Number of months to get daily data for
START_TIME = time.time()
TICKERS = Helper.get_tickers()                                # Load tickers from tickers.txt into list
START_DATE, END_DATE = Helper.get_dates(Months=GET_MONTHS)    # Get end date(current) and start date(-Get Months) for daily data

if not os.path.exists('Live-Data'):                           # Create folder to store live data if doesnt excists
    os.makedirs('Live-Data')

Data.Create_YFinance_Data(TICKERS, START_DATE, END_DATE)     # Create YFinance Data


# while loop that runs once a minute
while True:
    print("tick")
    time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))