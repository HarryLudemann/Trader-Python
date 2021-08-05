# Stock-Trader
[![Python Tests](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml/badge.svg)](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml)

### File Structure
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
            <td>Get_Yahoo_Trending</td>
            <td>Data/get_yahoo</td>
            <td>No args, scrapes trending stocks and information returns list of stock dictionary's</td>
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