import os
import sys
import inspect


def Load_Algorithms():
    """ function to get all classes in algorithms folder into a returned list """
    algos = []          # list to store classes

    # move directory to parent 
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir) 

    # get list of files in Algorithms directory into list
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir('Algorithms') if isfile(join('Algorithms', f))]

    # move path into Algorithms directory
    sys.path.insert(0, 'Algorithms') 

    for file in onlyfiles:
        if file.endswith('.py'):
            module = file[:-3]
            # import file as module from Algorithms directory
            module = __import__(module)
            test_algo = module.StockAlgorithm()
            test_algo.Init()
            algos.append(test_algo)

    return algos



def Load_Active_Algorithms(All_Algorithms, Current_Date):
    """ function to get all active classes in algorithms list into a returned list """
     # get list of stocks where current date is within start and end date (optional)
    ActiveStockAlgorithms = []      # list of Algorithm Objects that dates are within range
    for stock_algo in All_Algorithms:
        algo_start = stock_algo.StartDate
        algo_end = stock_algo.EndDate
        if (algo_end != None):      # if end date is none, hasnt been set
            if algo_start <= Current_Date and algo_end >= Current_Date:
                ActiveStockAlgorithms.append(stock_algo)    # add active stock
        else:
            if algo_start <= Current_Date:
                ActiveStockAlgorithms.append(stock_algo)    # add active stock
        
    return ActiveStockAlgorithms

def Loaf_Inactive_Algorithms(All_Algorithms, Current_Date):
    """ function to get all inactive classes in algorithms list into a returned list """
    # get list of stocks where current date is before start and end date
    InactiveStockAlgorithms = []      # list of Algorithm Objects that dates are within range
    for stock_algo in All_Algorithms:
        algo_start = stock_algo.StartDate
        algo_end = stock_algo.EndDate
        if (algo_end != None):      # if end date is none, hasnt been set
            if algo_start <= Current_Date and algo_end <= Current_Date:
                InactiveStockAlgorithms.append(stock_algo)
        else:
            if algo_start <= Current_Date:
                InactiveStockAlgorithms.append(stock_algo)

    return InactiveStockAlgorithms