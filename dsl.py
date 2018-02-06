'''
Created on 6 Feb 2018

@author: Alexei Figueroa

'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from functools import reduce

FS=44100.0
T=0.01
DT=1.0/44100



def white_noise_adder(mu,sigma):
    """
    Closure that returns a function that adds
    white noise determined by mu and sigma 
    """
    def add_noise(signal):
        return signal+np.random.normal(mu,sigma,len(signal))
    return add_noise

def sine_adder(f):
    """
    Closure returning a function that adds a 
    sine wave to a signal
    """
    def add_sine(signal):
        t=np.arange(0,T,DT)
        return signal+np.sin(f*2*np.pi*t)
    return add_sine

def lp_filter(order,cutoff):
    """
    Closure that returns a low pass filter function to 
    be applied on a signal
    """
    def filter_func(signal):
        b,a=scipy.signal.butter(order, cutoff/FS)
        return np.real(scipy.signal.lfilter(b, a, signal))
    return filter_func

def fold(*funcs):
    """
    Function that composes an arbitrary number of functions
    """
    def f_of_g(f,g):
        return lambda x:f(g(x))
    return reduce(f_of_g,funcs,lambda x:x)

        
def plotter():
    """
    Closure that returns a function that plots a signal
    """
    def plot_signal(signal):
        plt.plot(signal)
        plt.show()
        return signal
    return plot_signal


class AdditiveSynthTool():
    def __init__(self):
        """
        Constructor: the  only property is a signal.
        """
        self.signal=np.zeros_like(np.arange(0,T,DT))
    
    def add(self,f):
        """
        Adds a sinusoid of a given frequency to the signal
        @f: Frequency of the sinusoidal to be added to the signal
        """
        t=np.arange(0,T,DT)
        self.signal+=np.sin(f*2*np.pi*t)
        return self
    def low_pass(self,order,cutoff):
        """
        Low passes the signal
        @order: Order of the Butterworth low pass filter
        @cuttoff: Cuttoff frequencies of the Butterworth lp filter
        """
        b,a=scipy.signal.butter(order, cutoff/FS)
        self.signal=np.real(scipy.signal.lfilter(b, a, self.signal))
        return self
    def apply(self,func):
        """
        Applies an arbitrary function to the signal
        @func: Function to be applied on the signal
        """
        self.signal=func(self.signal)
        return self
    def plot_stage(self):
        """
        Plots the signal
        """
        plt.plot(self.signal)
        plt.show()
        return self
    
def main():
    
    """
    Object oriented DSL using the AdditiveSynthTool object
    """
    one_sigma=white_noise_adder(0, 1) #Create a function that adds white noise with mean 0 and variance 1
    a=AdditiveSynthTool()           
    #Creating the pipeline of a synthesizer
    a.add(440).add(490).plot_stage().apply(one_sigma).plot_stage().apply(lambda x:2*x).plot_stage()
    #Another example using a filter
    b=AdditiveSynthTool()
    b.add(440).add(6000).apply(lambda x:2*x).apply(one_sigma).low_pass(2, 1000.0).plot_stage()
    
    
    
    """
    Functional DSL example
    """
    signal=np.zeros_like(np.arange(0,T,DT)) #Empty signal
    
    one_sigma=white_noise_adder(0, 1)         #White noise
    
    times_2=lambda x:2*x                    #Amplifier with gain 2
    low_freq=sine_adder(440)                #Low frequency sine wave
    high_freq=sine_adder(6000)              #High frequency sine wave
    lp=lp_filter(2,1000.0)                  #Low pass filter
    
    #Build the pipeline, the execution goes from right to left of the pipeline
    synth=fold(plotter(),lp,plotter(),one_sigma,times_2,plotter(),high_freq,low_freq) 
    synth(signal)
    
if __name__=="__main__":
    main()
