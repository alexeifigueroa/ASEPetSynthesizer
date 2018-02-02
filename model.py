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


class synthesizerModel(object):
    '''
    This class represents the domain logic of the
    synthesizer, it holds the signal generator.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.vibrato=False
        self.sineGenerator=SignalGenerator(window_on=False, Fs=44100,frameSize=4410.0/44100)
    
    def initializeGenerator(self):
        """
        This method initializes the signal generator with the model accessible parameters , 
        in this case only vibrato
        """
        self.sineGenerator=SignalGenerator(window_on=self.__vibrato, Fs=44100,frameSize=4410.0/44100)
    def switchOnSignalChannels(self,keys):
        """
        This method updates the signal generator and makes it play on all the mixer channels.
        """
        self.sineGenerator.setKeys(keys)
        self.sineGenerator.generate()
        
    """
    Getters,Setters and properties
    """
    def getVibrato(self):
        return self.__vibrato
    def setVibrato(self,vibrato):
        self.__vibrato=vibrato
    vibrato=property(getVibrato,setVibrato)
    