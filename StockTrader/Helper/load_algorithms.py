import os
import sys
import inspect


def load_algorithms():
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





