# Stock-Trader

### File Structure
* **Algorithms** - contains created algorithms
* **Tests** - Contains pytests
* **.github** - Folder containing github actions
* **Live-Data** - Contains files saved and created in runtime   
* **start. py** - main script    
* **display. py** - script to display data
* **tester. py** - not needed used to test functions
* **tickers.txt** - list of tickers to collect information on     
* **StockTrader** - Contains Modules:
    * **Data** - Module to download data from different sources    
    * **Helper** - Module to clean data or load local data     
    * **Trader** - Module containing main Trading features 

### Custom Modules:
##### Helper Functions
<table>
    <thead>
        <tr>
            <th>File</th>
            <th>Name</th>
            <th>Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Helper/dates</td>
            <td>get_dates</td>
            <td>Given integer, returns 2 strings of start and end date as yy-mm-dd. start date as current date minus given integer months and start as current date</td>
        </tr>
        <tr>
            <td>Helper/load_data</td>
            <td>get_tickers</td>
            <td>Given no arguments, loads tickers from tickers.txt (Ticker on each line) and returns list</td>
        </tr>
        <tr>
            <td>Helper/visualize</td>
            <td>plot_ohlc</td>
            <td>given cleaned dataframe, plots ohlc</td>
        </tr>
    </tbody>
</table>

##### Data Functions
<table>
    <thead>
        <tr>
            <th>File</th>
            <th>Name</th>
            <th>Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data/get_yfinance</td>
            <td>get_yfinance_period</td>
            <td>Given interval (eg 1d), ticker, start date and end date gets stock data OHLC and volume from yfinance</td>
        </tr>
        <tr>
            <td>Data/get_yfinance</td>
            <td>get_yfinance_date</td>
            <td>Given interval (eg 1m), ticker and period (eg 7d) gets stock data OHLC and volume from yfinance</td>
        </tr>
        <tr>
            <td>Data/get_yfinance</td>
            <td>clean_yfinance_df</td>
            <td>Given tickers and dataframe from a yfinance array and returns list of cleaned dataframes</td>
        </tr>
        <tr>
            <td>Data/get_yfinance</td>
            <td>Create_YFinance_Data</td>
            <td>Given tickers, start date and end date gets daily and minute(Set to 7 days) data from yfinance to Live-Data</td>
        </tr>
        <tr>
            <td>Data/get_yfinance</td>
            <td>Update_YFinance_Minute</td>
            <td>Given tickers, Gets minute data and adds to existing minute data</td>
        </tr>
        <tr>
            <td>Data/get_yfinance</td>
            <td>Update_YFinance_Daily</td>
            <td>Given tickers, Gets daily data and adds to existing daily data</td>
        </tr>
        <tr>
            <td>Data/get_yahoo</td>
            <td>get_yahoo_trending</td>
            <td>No args, scrapes trending stocks and information returns list of stock dictionary's</td>
        </tr>
    </tbody>
</table>




### Tests:
<table>
    <thead>
        <tr>
            <th>File</th>
            <th>Name</th>
            <th>Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Test/test_get_yahoo.py</td>
            <td>test_yahoo_trending</td>
            <td>Tests that get_yahoo_trending returns 30 items</td>
        </tr>
        <tr>
            <td>Test/test_algorithm.py</td>
            <td>test_algorithm</td>
            <td>Tests that algorithms abstract class instantiates with appropriate fields</td>
        </tr>
    </tbody>
</table>


[![Python Tests](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml/badge.svg)](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml)