import os
# import tickers.txt as list using context manager
# read tickers.txt and save to list
# print list
def Get_Tickers():
    """
    loads tickers from tickers.txt into a returned list
    :return list:
    """
    # with open(os.path.join(os.path.dirname(__file__), 'tickers.txt'), 'r') as f:
    #     return f.read().splitlines()
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'templates')) # Move Path to main 
    with open('tickers.txt', 'r') as tickers:
        tickers = tickers.read()
        tickers = tickers.split('\n')
        return tickers


