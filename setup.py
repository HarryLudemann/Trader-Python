from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Run/Backtest/Create Easy Python Trading Algorithms'
LONG_DESCRIPTION = 'A package package that allows creating trading algorithms easy to write, backtest and run.'

# Setting up
setup(
    name="trader-python",
    version=VERSION,
    author="Hazzahx (Harry Ludemann)",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'yfinance', 'requests'],
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