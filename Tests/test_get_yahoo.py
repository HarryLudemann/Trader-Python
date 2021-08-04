# Modules
import os
import sys
import inspect

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

# Custom Modules
from StockTrader import Data


def test_yahoo_trending():
    """Checks that get yahoo trending returns 30 items"""
    assert len( Data.get_yahoo_trending() ) == 30
