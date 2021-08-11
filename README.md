# Trader
[![Python Tests](https://github.com/HarryLudemann/Stock-Trader-Python/actions/workflows/python-package.yml/badge.svg)](https://github.com/HarryLudemann/Stock-Trader/actions/workflows/python-package.yml)

Module to easily write, run and back test algorithms against current list of data sources below.

### Install Setup:
```
pip install trader-python
```
### Functions:
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
            <td>backtest</td>
            <td>trader</td>
            <td>Given algorithm object backtest's getting information and passing to objects on_data, returns nothing</td>
        </tr>
        <tr>
            <td>run</td>
            <td>trader</td>
            <td>Given algorithm object run's getting information and passing to objects on_data, returns nothing</td>
        </tr>
    </tbody>
</table>

### Data sources
* Yfinance: 1m, 5m, 15m, 30m, 60m, 1d, 1w, 1m (Back testing doesn't use start/end date when using a minute interval (1m, 5m, 15m) auto set to get last 7 days of info)
* Alpha Vantage (requires API_KEY var):  1m, 5m, 15m, 30m, 60m, 1d, 1w, 1m (Back testing doesn't use start and end dates)

### Creating Algorithm Classes:
#### Algorithm(StockAlgorithm):
##### Init Method:     
    Used to set fields
    **Name**  =                     # Name of algorithm     
    **Symbol** =                    # Stock Ticker     
    **StartDate** =                 # Start Date for algorithm (Some data sources don't use)     
    **EndDate** =                   # End Date for algorithm (Some data sources don't use)     
    **Cash** =                      # Cash allowed for algorithm to use     
    **Data_Source** =               # data Source for stock information (Check data sources)     
    **API_KEY** =                   #if data source requires api key
    **Adjusted** =                  # Wether to use Adjusted data (Some data sources don't use)  - Default False     
    **Interval** =                  # Interval for data eg 1m, 5m, 1d, 1m     
    **Back_Test** =                 # Wether to the strategy is to back test or to run  - Default False     

##### on_data Method:  
    Method passed data tuple, method called on new data

##### stats Method:  
    Method Called when finished running or back testing, passed nothing

##### Example:
```python
from trader import StockAlgorithm, run
from datetime import datetime

class Algorithm(StockAlgorithm):
    """ Example Algorithm to Run """

    def init(self):
        self.Active =True
        self.Name = "Example Algo"
        self.Symbol = "TSLA"
        self.StartDate = datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'yfinance'
        self.Adjusted = False
        self.Interval = "1m"

    def on_data(self, data):
        print(data)
        
    def stats(self):
        print(self.Name, 'Finished with', self.Cash)


test_algo = Algorithm()
test_algo.init()

run([test_algo])
```

#### Algorithm(ForexAlgorithm):
##### Init Method:     
    Used to set fields
    Active =                        # Signal wether to run/backtest
    Name =                          # Name of algorithm
    From_Currency =                 # From Currency Ticker
    To_Currency =                   # To Currency Ticker
    StartDate =                     # Start Date for algorithm (Some datasources don't use)
    EndDate =                       # End Date for algorithm (Some datasources don't use)
    Cash =                          # Cash allowed for algorithm to use
    data_Source =                   # data Source for stock infomation (Check data sources)
    **API_KEY** =                   #if data source requires api key
    Interval =                      # Interval for data eg 1m, 5m, 1d, 1m

##### on_data Method:  
    Method passed data tuple, method called on new data

##### stats Method:  
    Method Called when finished running or back testing, passed nothing

##### Example:
```python
from trader import ForexAlgorithm, backtest
from datetime import datetime

class Algorithm(ForexAlgorithm):
    """ Example Algorithm to Run """

    def init(self):
        self.Active =True
        self.Backtest = True
        self.Name = "Example Algo"
        self.From_Currency = "USD"
        self.To_Currency = "NZD"
        self.StartDate = datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'yfinance'
        self.Adjusted = False
        self.Interval = "1m"

    def on_data(self, data):
        print(data)
        
    def stats(self):
        print(self.Name, 'Finished with', self.Cash)


test_algo = Algorithm()
test_algo.init()

backtest([test_algo])
```

### Development:
#### Adding data sources       
example function name:  get_{API}_{Stock/Forex/Crypto}   
returns df:
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

#### Tests:
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
            <td>test_stock_algorithm</td>
            <td>Test/test_algorithm.py</td>
            <td>Tests stock algorithm class instantiates with appropriate fields</td>
        </tr>
        <tr>
            <td>test_forex_algorithm</td>
            <td>Test/test_algorithm.py</td>
            <td>Tests forex algorithm class instantiates with appropriate fields</td>
        </tr>
    </tbody>
</table>
