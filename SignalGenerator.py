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

    def __init__(self,window_on=False, fs=44100,frame_size=4410.0/44100):
        '''
        Constructor
        @window_on: Boolean, states whether to apply a hanning window to the signal.
        @fs: Sampling frequency
        @frame_size: Number of samples per frame defaults to 100 milliseconds
        '''
        self.__fs=fs
        self.__ts=1.0/fs
        self.__frame_size=frame_size
        self.__keys={}
        self.__t0=0
        self.__run=False
        self.__active_keys={}
        self.__channels={}
        
        window=scipy.signal.hanning(int(frame_size*fs),True) if window_on else []
        self.generate_sounds(window)
    
    def generate(self):
        """
        This methods simulates the generation of the different 
        frequencies related to the keys by enabling the signal on the mixer
        through changing the volume.
        """
        if self.diff_keys(self.__active_keys):
            for k in self.__channels:
                self.__channels[k].set_volume(0)
            for k in self.__keys:
                self.__channels[k].set_volume(1.0/len(self.__keys))
            self.__active_keys=self.__keys
            
    
    def generate_sounds(self,w):
        """
        This method generates sine waves with the frequencies
        of the keys specified in CONSTANTS.keyMap, it also plays
        them on the mixer of pygame.
        
        @w: list, it defines whether the hanning window is 
            multiplied with the sine wave generated, this is used
            to simulate vibrato.
        """
        for k in CONSTANTS.keyMap:
            f=self.key_frequency(CONSTANTS.keyMap[k])   #Frequency of the piano key
            
            window = w if len(w) else 1.0               #Replace the step function when the window parameter is given 
            T=len(w)*self.__ts if len(w) else 1.0/f     #Resize the sine wave time to one period or the window time
            t=np.arange(0,T,self.__ts)                  #Create the time dimension
            
            #Create the wave applying the window with short int amplitude
            s=32767.0*np.sin(2*np.pi*f*t)*window         
            self.__channels[k]=pygame.mixer.find_channel(True)  #Book the channel
            sound = pygame.sndarray.make_sound(np.int16(s))     
            
            #mute the channel and play infinitely the sound
            self.__channels[k].set_volume(0.0)
            self.__channels[k].play(sound,loops=-1)
            
    def key_frequency(self,n):
        """
        Returns the frequency associated to a key number in a piano.
        @n: Key number in the piano
        """
        #0 =A=440Hz
        return np.power(2,(n-49)/12)*440#Hz
    
    def diff_keys(self,keys):
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
    def set_keys(self,keys):
        self.__keys=keys
