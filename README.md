# Trader
[![Python Tests](https://github.com/HarryLudemann/Stock-Trader-Python/actions/workflows/python-package.yml/badge.svg)](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml)

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
    * **Trader** - Module containing main Trading features 
* **Algorithms** - contains user created algorithm classes
* **Live-Data** - Contains files saved and created in runtime   
* **Tests** - Contains pytests
* **start. py** - main script to start Stock Trader   
* **display. py** - script to display data
* **tickers.txt** - list of tickers to collect information on     

### Custom Module Functions:
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
            <td>get_yfinance_stock</td>
            <td>Data/get_yfinance</td>
            <td>Given tickers, start and end date and interval Gets appropriate data and returns df</td>
        </tr>
        <tr>
            <td>get_yfinance_forex</td>
            <td>Data/get_yfinance</td>
            <td>Given to and from data, interval and start and end date Gets appropriate data and returns df</td>
        </tr>
        <tr>
            <td>get_alphav_stock</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given ticker, optionally interval optionally adjusted boolean returns df of stock data</td>
        </tr>
        <tr>
            <td>get_alphav_forex</td>
            <td>Data/get_alpha_vantage</td>
            <td>Given from and to currency and interval returns df of stock data</td>
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
            <td>test_algorithm</td>
            <td>Test/test_algorithm.py</td>
            <td>Tests that algorithms abstract class instantiates with appropriate fields</td>
        </tr>
    </tbody>
</table>


### Development:
##### Adding data sources
get_{API}_{Stock/Forex/Crypto} functions return df:
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
