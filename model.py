'''
Created on Jan 3, 2018

@author: alexei
'''
from SignalGenerator import SignalGenerator
class synthesizerModel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.vibrato=False
        self.sineGenerator=SignalGenerator(window_on=False, Fs=44100,frameSize=4410.0/44100)
        
    def getVibrato(self):
        return self.__vibrato
    def setVibrato(self,vibrato):
        self.__vibrato=vibrato
    vibrato=property(getVibrato,setVibrato)
    def initializeGenerator(self):
        self.sineGenerator=SignalGenerator(window_on=self.__vibrato, Fs=44100,frameSize=4410.0/44100)
    def switchOnSignalChannels(self,keys):
        self.sineGenerator.setKeys(keys)
        self.sineGenerator.generate()
    