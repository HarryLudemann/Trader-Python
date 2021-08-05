#import numpy as np
import matplotlib.pyplot as plt

# method to plot given ohlc data    
def Plot_Ohlc(df):
    """Plotting function for OHLC data"""
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.plot(df['Date'], df['Open'], color='red', label='Open')
    ax.plot(df['Date'], df['High'], color='green', label='High')
    ax.plot(df['Date'], df['Low'], color='blue', label='Low')
    ax.plot(df['Date'], df['Close'], color='black', label='Close')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='best')
    plt.show()