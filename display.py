# Modules
import Data
import pandas as pd

# Custom Modules
import Helper
import Data


TICKERS = Helper.get_tickers()                                # Load tickers from tickers.txt into list


def Plotting_Example():
    daily_data = pd.read_csv('Live-Data/daily_yfinance_data.csv')       # load yfinance daily data data from csv's
    cleaned_stocks = Data.clean_yfinance_df(TICKERS, daily_data)        # clean data
    Helper.plot_ohlc( cleaned_stocks[0].dropna() )                      # remove NaN values and plot data


if __name__ == "__main__":
    Plotting_Example()