'''
Created on Dec 19, 2017

@author: Alexei Figueroa
'''
import numpy as np
import pygame,scipy.signal,CONSTANTS



class SignalGenerator(object):
    '''
    This class simulates the signal generator
    of an Analogue Synthesizer
    '''

    def __init__(self,window_on=False, Fs=44100,frameSize=4410.0/44100):
        '''
        Constructor
        @window_on: Boolean, states whether to apply a hanning window to the signal.
        @Fs: Sampling frequency
        @frameSize: Number of samples per frame defaults to 100 milliseconds
        '''
        self.__Fs=Fs
        self.__Ts=1.0/Fs
        self.__frameSize=frameSize
        self.__keys={}
        self.__t0=0
        self.__run=False
        self.__activeKeys={}
        self.__channels={}
        
        window=scipy.signal.hanning(int(frameSize*Fs),True) if window_on else []
        self.generateSounds(window)
    
    def generate(self):
        """
        This methods simulates the generation of the different 
        frequencies related to the keys by enabling the signal on the mixer
        through changing the volume.
        """
        if self.diffKeys(self.__activeKeys):
            for k in self.__channels:
                self.__channels[k].set_volume(0)
            for k in self.__keys:
                self.__channels[k].set_volume(1.0/len(self.__keys))
            self.__activeKeys=self.__keys
            
    
    def generateSounds(self,w):
        """
        This method generates sine waves with the frequencies
        of the keys specified in CONSTANTS.keyMap, it also plays
        them on the mixer of pygame.
        
        @w: list, it defines whether the hanning window is 
            multiplied with the sine wave generated, this is used
            to simulate vibrato.
        """
        for k in CONSTANTS.keyMap:
            f=self.keyFreq(CONSTANTS.keyMap[k])
            T=1.0/f
            window=1
            if len(w)!=0:
                T=len(w)*self.__Ts
                window=w
            t=np.arange(0,T,self.__Ts)
            
            s=32767.0*np.sin(2*np.pi*f*t)*window
            self.__channels[k]=pygame.mixer.find_channel(True)
            sound = pygame.sndarray.make_sound(np.int16(s))
            
            self.__channels[k].set_volume(0.0)
            self.__channels[k].play(sound,loops=-1)
            
    def keyFreq(self,n):
        """
        Returns the frequency associated to a key number in a piano.
        @n: Key number in the piano
        """
        #0 =A=440Hz
        return np.power(2,(n-49)/12)*440#Hz
    
    def diffKeys(self,keys):
        """
        Returns True if the keys received as an argument are different
        from the keys that are generating sound in the mixer.
        
        @keys: Dictionary with keys mapping pygame.key_ constants to a boolean
                defining whether each key is pressed
        """
        if len(keys)!=len(self.__keys):
            return True
        for k in keys:
            if k not in self.__keys.keys():
                return True
            if keys[k]!=self.__keys[k]:
                return True
        return False
    """
    Getters and Setters
    """
    def setKeys(self,keys):
        self.__keys=keys
