from StockTrader import Helper


algos = Helper.get_algorithms()         # list of Algorithm Objects

for algo in algos:
    algo.on_data()