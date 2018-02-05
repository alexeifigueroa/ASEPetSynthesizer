'''
Created on Feb 5, 2018

@author: Alexei Figueroa
'''
import CONSTANTS,time

def log_arguments(f):
    """
    @f: Function to be wrapped with the logging of it's arguments
    """
    def logger(*args,**kwargs):
        """
        wrapping function, it logs the arguments of the decorated function
        """
        if CONSTANTS.LOG_ARGUMENTS:
            #print("Function "+f.__name__+" called:")
            print("Positional Arguments ")
            for a in args:
                print(a)
            print("keyword arguments ")
            for k,v in kwargs.items():
                print(k+" = "+v)
        return f(*args,**kwargs)
    return logger

def time_execution(f):
    """
    @f: Function to be wrapped with the logging of it's execution time
    """
    def timing_wrapper(*args,**kwargs):
        """
        wrapping function, it logs the execution time of the decorated function
        """
        if CONSTANTS.TIME_EXECUTION:
            start=time.time()
        f(*args,**kwargs)
        if CONSTANTS.TIME_EXECUTION:
            end=time.time()
            print("Execution time: "+str(end-start)+" seconds.")
    return timing_wrapper
