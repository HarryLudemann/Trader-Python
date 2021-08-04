# Stock-Trader

### File Structure
* Algorithm - contains created algorithms
* .github - Folder containing github actions
* Data - Module to download data from different sources    
* Helper - Module to clean data or load local data     
* Live-Data - Contains files saved and created in runtime    
* Trader - Module containing main Trading features
* start. py - main script    
* tickers.txt - list of tickers to collect information on     

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