from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Run/Backtest/Create Easy Python Trading Algorithms'
LONG_DESCRIPTION = 'A package that allows easy to write, run and backtest algorithms for stocks, forex and crypto from pre-written data sources eg. alpha vantage, yfinance'

# Setting up
setup(
    name="trader-python",
    version=VERSION,
    author="Harry Ludemann",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'yfinance', 'alpha_vantage', 'requests'],
    keywords=['python', 'harryludemann', 'trader', 'backtest', 'trader-python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        # "Operating System :: Unix",
        # "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)