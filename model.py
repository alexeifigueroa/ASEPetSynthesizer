'''
Created on Jan 3, 2018

@author: Alexei Figueroa

This module holds the domain logic behind the synthesizer
it supports an analogue sine wave generator.

TODO: 
* add amplitude modification of the signals.
* add filtering of the signals.
* add voltage regulated filter.
'''
from SignalGenerator import SignalGenerator


class SynthesizerModel(object):
    '''
    This class represents the domain logic of the
    synthesizer, it holds the signal generator.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.vibrato=False
        self.sineGenerator=SignalGenerator(window_on=False, fs=44100,frame_size=4410.0/44100)
    
    def initialize_generator(self):
        """
        This method initializes the signal generator with the model accessible parameters , 
        in this case only vibrato
        """
        self.sineGenerator=SignalGenerator(window_on=self.__vibrato, fs=44100,frame_size=4410.0/44100)
    def switch_on_signal_channels(self,keys):
        """
        This method updates the signal generator and makes it play on all the mixer channels.
        """
        self.sineGenerator.set_keys(keys)
        self.sineGenerator.generate()
        
    """
    Getters,Setters and properties
    """
    def get_vibrato(self):
        return self.__vibrato
    def set_vibrato(self,vibrato):
        self.__vibrato=vibrato
    vibrato=property(get_vibrato,set_vibrato)
    
