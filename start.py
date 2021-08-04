# Modules
import os

# Custom Modules
import Data
import Helper

# Declare Varibles
tickers = Helper.get_tickers()                                # Period for data (1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max)
# get start and end date 
get_months = 1                                                # Number of months to get daily data for
start_date, end_date = Helper.get_dates(Months=get_months)    # Get the start(current) and end date(-Get Months) for daily data

# Create Live-Data Directory if Doesnt exsist
if not os.path.exists('Live-Data'):                          
    os.makedirs('Live-Data')

# Create YFinance Data
Data.Create_YFinance_Data(tickers, start_date, end_date)


# minute_data = pd.read_csv('Live-Data/minute_stock_data.csv')
# daily_data = pd.read_csv('Live-Data/daily_stock_data.csv')

# cleaned_stocks = Data.clean_yfinance_df(tickers, daily_data)

# Helper.plot_ohlc( cleaned_stocks[0].dropna() )      # remove NaN values and plot data

