# Custom Modules
import Data
import Helper

def test_yahoo_trending():
    """Checks that get yahoo trending returns 30 items"""
    assert len(get_yahoo_trending()) == 30