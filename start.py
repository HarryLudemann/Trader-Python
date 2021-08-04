# Modules
import os
import pandas as pd

# Custom Modules
import Data
import Helper

# Initialize 
GET_MONTHS = 1                                                # Number of months to get daily data for
TICKERS = Helper.get_tickers()                                # Load tickers from tickers.txt into list
START_DATE, END_DATE = Helper.get_dates(Months=GET_MONTHS)    # Get end date(current) and start date(-Get Months) for daily data

if not os.path.exists('Live-Data'):                           # Create folder to store live data if doesnt excists
    os.makedirs('Live-Data')

Data.Create_YFinance_Data(TICKERS, START_DATE, END_DATE)     # Create YFinance Data




