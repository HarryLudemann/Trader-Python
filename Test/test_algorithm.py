# Modules
import os
import sys
import inspect

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

# Custom Modules
import StockTrader


def test_algorithm():
    """Checks the algorthm abstract class initializes properly returning value"""

    class TestAlgo(StockTrader.Algorithm):
        """ Test Algorithm that returns test value in on data"""
        def on_data(self):
            return "Test"

    assert TestAlgo(name="Test", symbol="TEST", start_date="2018-01-01", end_date="2018-01-02").on_data() == "Test"
