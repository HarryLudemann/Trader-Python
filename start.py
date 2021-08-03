# Custom Modules
import StockTrader
import Data
import Helper

# Declare Varibles
tickers = Helper.get_tickers()                                # gets list of tickers from file
interval = '1d'                                               # Interval for data (1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo)
period = '5d'                                                 # Period for data (1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max)
get_months = 1                                                # Number of months to get data for
start_date, end_date = Helper.get_dates(Months=get_months)    # Get the start(current) and end date(-Get Months)

# Get Stock Data
data = Data.get_yfinance_date(interval, tickers, start_date, end_date)   # returns numpy array of data using dates

data = Data.get_yfinance_period(interval, tickers, period)               # returns numpy array of data using period

# save as csv
data.to_csv('Live-Data/stock_data.csv')

