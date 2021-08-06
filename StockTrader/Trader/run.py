# modules
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from StockTrader import Data

def Run(Algorithm):
    """ Get and pass infomation to stock """
    if Algorithm.Data_Source == 'AlphaV':   # if using Alpha Vantage
        if EST_TIME >= '04:00:00' and EST_TIME <= '20:00:00':   # check if EST_TIME is within 4 am and 8 pm
                print("Within Trading Times")
