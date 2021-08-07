# Stock-Trader
[![Python Tests](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml/badge.svg)](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml)

### Setup:
##### Create .env:
Create .env file in main directory (containing start.py) with alpha vantage key like so
```
ALPHA_VANTAGE_KEY=eafaapikey
```

### Creating Algorithms:
Create algorithms and store in Algorithm folder, currently contains examples, algorithms file can be named anything.

#### Algorithm(Trader.StockAlgorithm) Class:
##### Data Sources: 
    **YFinance** - Python module YFinance retrieving yahoo information (Back testing doesn't use start/end date when using a minute interval (1m, 5m, 15m) auto set to get last 7 days of info)     
    **AlphaV** - Get information from Alpha Vantage API (back testing doesn't use start/end date used against all info retrieved)     
    
##### Init Method:     
    Used to set fields
    **Name**  =                     # Name of algorithm     
    **Symbol** =                    # Stock Ticker     
    **StartDate** =                 # Start Date for algorithm (Some Data sources don't use)     
    **EndDate** =                   # End Date for algorithm (Some Data sources don't use)     
    **Cash** =                      # Cash allowed for algorithm to use     
    **Data_Source** =               # Data Source for stock information (Check Data sources)     
    **Adjusted** =                  # Wether to use Adjusted data (Some Data sources don't use)  - Default False     
    **Interval** =                  # Interval for data eg 1m, 5m, 1d, 1m     
    **Save_Data** =                 # Wether to save the information collected for algorithm  - Default False     
    **Back_Test** =                 # Wether to the strategy is to back test or to run  - Default False     

##### on_data Method:  
    Method passed data tuple, method called on new data

##### stats Method:  
    Method Called when finished running or back testing, passed nothing

#### Algorithm(Trader.ForexAlgorithm) Class:
##### Data Sources: 
    **YFinance** - Python module YFinance retrieving yahoo information    
    **AlphaV** - Get information from Alpha Vantage API    
    
##### Init Method:     
    Used to set fields
    Active =                        # Signal wether to run/backtest
    Name =                          # Name of algorithm
    From_Currency =                 # From Currency Ticker
    To_Currency =                   # To Currency Ticker
    StartDate =                     # Start Date for algorithm (Some Datasources don't use)
    EndDate =                       # End Date for algorithm (Some Datasources don't use)
    Cash =                          # Cash allowed for algorithm to use
    Data_Source =                   # Data Source for stock infomation (Check Data sources)
    Interval =                      # Interval for data eg 1m, 5m, 1d, 1m
    Save_Data =                     # Wether to save the infomation collected for algorithm  - Default False
    Back_Test =                     # Wether to the strategy is to back test or to run  - Default False

##### on_data Method:  
    Method passed data tuple, method called on new data

##### stats Method:  
    Method Called when finished running or back testing, passed nothing


### Limitations

##### Back Testing
* Yfinance intervals: 1m, 5m, 15m, 30m, 60m, 1d, 1w, 1m
* Yfinance Back testing doesn't use start/end date when using a minute interval (1m, 5m, 15m) auto set to get last 7 days of info
* Alpha Vantage Intervals: 1m, 5m, 15m, 30, 60m, 1d, 1w, 1m
* Alpha Vantage Back testing doesn't use start and end dates


### File Structure:
* **StockTrader** - Contains Main Modules:
    * **Data** - Module to download data from different sources    
    * **Helper** - Module to clean data or load local data     
    * **Trader** - Module containing main Trading features 
* **Algorithms** - contains user created algorithm classes
* **Live-Data** - Contains files saved and created in runtime   
* **Tests** - Contains pytests
* **start. py** - main script to start Stock Trader   
* **display. py** - script to display data
* **tickers.txt** - list of tickers to collect information on     

### Custom Modules:
##### Helper Functions
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>File</th>
            <th>Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Get_Dates</td>
            <td>Helper/dates</td>
            <td>Given integer, returns 2 strings of start and end date as yy-mm-dd. start date as current date minus given integer months and start as current date</td>
        </tr>
        <tr>
            <td>Get_Tickers</td>
            <td>Helper/load_data</td>
            <td>Given no arguments, loads tickers from tickers.txt (Ticker on each line) and returns list</td>
        </tr>
        <tr>
            <td>Plot_Ohlc</td>
            <td>Helper/visualize</td>
            <td>given cleaned dataframe, plots ohlc</td>
        </tr>
        <tr>
            <td>Load_Algorithms</td>
            <td>Helper/load_algorithms</td>
            <td>given nothing, returns list of objects from Algorithms dir</td>
        </tr>
        <tr>
            <td>Load_Active_Algorithms</td>
            <td>Helper/load_algorithms</td>
            <td>given all algorithms list and current date, returns list of active Algorithm objects</td>
        </tr>
        <tr>
            <td>Load_Inactive_Algorithms</td>
            <td>Helper/load_algorithms</td>
            <td>given all algorithms list and current date, returns list of inactive Algorithm objects</td>
        </tr>
    </tbody>
</table>


##### Trader Functions
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>File</th>
            <th>Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>BackTest</td>
            <td>Trader/backtest</td>
            <td>Given algorithm object back tests, returns nothing</td>
        </tr>
    </tbody>
</table>

##### Data Functions
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>File</th>
            <th>Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Get_Yfinance_Period</td>
            <td>Data/get_yfinance</td>
            <td>Given interval (eg 1d), ticker, start date and end date gets stock data OHLC and volume from yfinance</td>
        </tr>
        <tr>
            <td>Get_Yfinance_Date</td>
            <td>Data/get_yfinance</td>
            <td>Given interval (eg 1m), ticker and period (eg 7d) gets stock data OHLC and volume from yfinance</td>
        </tr>
        <tr>
            <td>Clean_Yfinance_Df</td>
            <td>Data/get_yfinance</td>
            <td>Given tickers and dataframe from a yfinance array and returns list of cleaned dataframes</td>
        </tr>
        <tr>
            <td>Create_YFinance_Data</td>
            <td>Data/get_yfinance</td>
            <td>Given tickers, start date and end date gets daily and minute(Set to 7 days) data from yfinance to Live-Data</td>
        </tr>
        <tr>
            <td>Update_YFinance_Minute</td>
            <td>Data/get_yfinance</td>
            <td>Given tickers, Gets minute data and adds to existing minute data</td>
        </tr>
        <tr>
            <td>Update_YFinance_Daily</td>
            <td>Data/get_yfinance</td>
            <td>Given tickers, Gets daily data and adds to existing daily data</td>
        </tr>
        <tr>
            <td>Get_YFinance_Stock</td>
            <td>Data/get_yfinance</td>
            <td>Given tickers, start and end date and interval Gets appropriate data and returns df</td>
        </tr>
        <tr>
            <td>Get_YFinance_Forex</td>
            <td>Data/get_yfinance</td>
            <td>Given to and from data, interval and start and end date Gets appropriate data and returns df</td>
        </tr>
        <tr>
            <td>Get_Yahoo_Trending</td>
            <td>Data/get_yahoo</td>
            <td>No args, scrapes trending stocks and information returns list of stock dictionary's</td>
        </tr>
        <tr>
            <td>Get_AlphaV_Stock</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given ticker, optionally interval optionally adjusted boolean returns df of stock data</td>
        </tr>
        <tr>
            <td>Get_AlphaV_Forex</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given from and to currency and interval returns df of stock data</td>
        </tr>
        <tr>
            <td>Get_AlphaV_Stock</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given ticker, interval and optionally adjusted boolean returns df of stock data</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Intraday</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves data to Live_data using alpha vantages TIME_SERIES_INTRADAY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Intraday_Ext</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves  data to Live_data using alpha vantages TIME_SERIES_INTRADAY_EXTENDED api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Daily</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves  data to Live_data using alpha vantages TIME_SERIES_DAILY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Daily_Adj</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves  data to Live_data using alpha vantages TIME_SERIES_DAILY_ADJUSTED api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Weekly</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves  data to Live_data using alpha vantages TIME_SERIES_WEEKLY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Weekly_Adj</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves  data to Live_data using alpha vantages TIME_SERIES_WEEKLY_ADJUSTED api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Monthly</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves  data to Live_data using alpha vantages TIME_SERIES_MONTHLY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Stock_Monthly_Adj</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given Stock Ticker saves  data to Live_data using alpha vantages TIME_SERIES_MONTHLY_ADJUSTED api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Forex_Exchange_Rate</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given from and to currency saves  data to Live_data using alpha vantages CURRENCY_EXCHANGE_RATE api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Forex_FX_Intraday</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given from, to currency and interval saves  data to Live_data using alpha vantages FX_INTRADAY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Forex_FX_Daily</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given from and to symbol saves  data to Live_data using alpha vantages FX_DAILY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Forex_FX_Weekly</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given from and to symbol saves  data to Live_data using alpha vantages FX_WEEKLY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Forex_FX_Monthly</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given from and to symbol saves  data to Live_data using alpha vantages FX_MONTHLY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Crypto_Exchange_Rate</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given symbol and market returns 3 strings from alpha vantages CURRENCY_EXCHANGE_RATE api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Crypto_Intraday</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given symbol market and interval saves  data to Live_data using alpha vantages CRYPTO_INTRADAY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Crypto_Daily</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given symbol and market saves  data to Live_data using alpha vantages DIGITAL_CURRENCY_DAILY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Crypto_Weekly</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given symbol and market saves  data to Live_data using alpha vantages DIGITAL_CURRENCY_WEEKLY api returns df</td>
        </tr>
        <tr>
            <td>Get_Alpha_Crypto_Monthly</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given symbol and market  saves  data to Live_data using alpha vantages DIGITAL_CURRENCY_MONTHLY api returns df</td>
        </tr>
    </tbody>
</table>


     
    
### Tests:
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>File</th>
            <th>Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>test_yahoo_trending</td>
            <td>Test/test_get_yahoo.py</td>
            <td>Tests that get_yahoo_trending returns 30 items</td>
        </tr>
        <tr>
            <td>test_algorithm</td>
            <td>Test/test_algorithm.py</td>
            <td>Tests that algorithms abstract class instantiates with appropriate fields</td>
        </tr>
    </tbody>
</table>


### Development:

Get_{API}_{Stock/Forex/Crypto} functions return df:
```
                      open   high    low  close
Datetime
2021-08-06 21:28:00  1.426  1.426  1.426  1.426
2021-08-06 21:27:00  1.426  1.426  1.426  1.426
2021-08-06 21:26:00  1.426  1.426  1.426  1.426
2021-08-06 21:25:00  1.426  1.426  1.426  1.426
2021-08-06 21:24:00  1.426  1.426  1.426  1.426
2021-08-06 21:23:00  1.426  1.426  1.426  1.426
2021-08-06 21:22:00  1.426  1.426  1.426  1.426
2021-08-06 21:21:00  1.426  1.426  1.426  1.426
2021-08-06 21:20:00  1.426  1.426  1.426  1.426
2021-08-06 21:19:00  1.426  1.426  1.426  1.426
```