# Modules
import os           # for file operations
import time         # for sleep - scheduler
from datetime import datetime     # get current date
from pytz import timezone   # timezones

# Custom Modules
from StockTrader import Helper
from StockTrader import Data

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
#ActiveAlgorithms = Helper.Load_Active_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE)   # list of Active Algorithms

# backtest method
InActive_Algorithms = Helper.Loaf_Inactive_Algorithms(All_Algorithms=Algorithms, Current_Date=START_DATE)
for algorithm in InActive_Algorithms:
    print("Starting Backtesting:")
    # get data from appropriate source
    if algorithm.Data_Source == 'AlphaV':   # if using Alpha Vantage
        stock_df = Data.Get_AlphaV_Stock(algorithm.Symbol, interval=algorithm.Interval, Adjusted=algorithm.Adjusted)
        start_date = stock_df['timestamp'].iloc[0]
        end_date = stock_df['timestamp'].iloc[-1]

        print('Backtesting:', algorithm.Symbol, ':', start_date, 'to', end_date)
        # iterate over each stock and pass tuple to algorithms on_data method
        for stock in stock_df.iterrows():
            algorithm.on_data(stock)

        if algorithm.Save_Data:
            stock_df.to_csv('Live-Data/Stock/' + algorithm.Name.strip() + '.csv')
        print('Finished', algorithm.Symbol, ':', start_date, 'to', end_date)


    elif algorithm.Data_Source == 'YFinance':   # if using YFinance 
        stock_df = Data.Get_YFinance_Stock(algorithm.Symbol, algorithm.StartDate, algorithm.EndDate, algorithm.Interval)
        # get first and last value
        start_date = stock_df.index[0]
        end_date = stock_df.index[-1]

        print('Backtesting:', algorithm.Symbol, ':', start_date, 'to', end_date)
        # iterate over each stock and pass tuple to algorithms on_data method
        for stock in stock_df.iterrows():
            algorithm.on_data(stock)

        if algorithm.Save_Data:
            stock_df.to_csv('Live-Data/Stock/' + algorithm.Name.strip() + '.csv')

        print('Finished', algorithm.Symbol, ':', start_date, 'to', end_date)

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