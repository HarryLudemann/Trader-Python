from trader import StockAlgorithm, backtest
from datetime import datetime

open_data = []
open_data2 = []


class Algorithm(StockAlgorithm):
    """ Example Algorithm to Run """

    def init(self):
        self.Active =True
        self.Name = "Example Algo"
        self.Symbol = "TSLA"
        self.StartDate = datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'alphav'
        self.API_KEY = '7PGWISTN90FB9RGV'              # Alpha Vantage API key
        self.Adjusted = False
        self.Interval = "1m"

    def on_data(self, data):
        open_data.append(data)
        
    def stats(self):
        return self.Name, 'Finished with', self.Cash


class Algorithm2(StockAlgorithm):
    """ Example Algorithm to Run """

    def init(self):
        self.Active = True
        self.Name = "Example Algo"
        self.Symbol = "TSLA"
        self.StartDate = datetime.now().strftime("%Y-%m-%d") # current time
        self.Cash = 100000
        self.Data_Source = 'alphav'
        self.API_KEY = '7PGWISTN90FB9RGV'              # Alpha Vantage API key
        self.Adjusted = False
        self.Interval = "1m"

    def on_data(self, data):
        open_data2.append(data)
        
    def stats(self):
        return self.Name, 'Finished with', self.Cash



import asyncio

async def main():
    test = Algorithm()
    test.init()
    test2 = Algorithm2()
    test2.init()
    div1 = loop.create_task( backtest(test2) )
    div2 = loop.create_task( backtest(test) )
    await asyncio.wait([div1, div2])
    return div1, div2


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        #loop.set_debug(1)
        d1, d2 = loop.run_until_complete(main())
        print(d1.result())
        print(d2.result())
    except Exception as e:
        print(e)
    finally:
        loop.close()