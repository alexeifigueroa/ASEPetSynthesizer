'''
Created on Dec 19, 2017

@author: alexei
'''
import numpy as np
import pygame,scipy.signal

keyMap={      pygame.K_a:49,    # A -> A
              pygame.K_w:50,    # W -> A#
              pygame.K_s:51,    # S -> B
              pygame.K_d:52,    # D -> C
              pygame.K_r:53,    # R -> C#
              pygame.K_f:54,    # F -> D
              pygame.K_t:55,    # T -> D#
              pygame.K_g:56,    # G -> E
              pygame.K_h:57,    # H -> F
              pygame.K_u:58,    # U -> F#
              pygame.K_j:59,    # J -> G
              pygame.K_i:60,    # I -> G#
              pygame.K_k:61,    # K -> A
              pygame.K_o:62,    # O -> A#
              pygame.K_l:63    # L -> B
              }

class SignalGenerator(object):
    '''
    This class simulates the signal generator
    of an Analogue Synthesizer
    '''

    def __init__(self,window_on=False, Fs=44100,frameSize=4410.0/44100):
        '''
        Constructor
        '''
        self.__Fs=Fs
        self.__Ts=1.0/Fs
        self.__frameSize=frameSize
        self.__keys={}
        self.__t0=0
        self.__run=False
        #self.__channel=pygame.mixer.Channel(0)
        self.__activeKeys={}
        b={}
        a={}
        self.__b, self.__a = scipy.signal.butter(8, 0.5, 'low', analog=False)
        
        
        #window=[]
        self.__channels={}
        if window_on:
            window=scipy.signal.hanning(int(frameSize*Fs),True)
            self.generateSounds(window)
        else:
            self.generateSounds([])
    
    def generate(self):
        if self.diffKeys(self.__activeKeys):
            for k in self.__channels:
                self.__channels[k].set_volume(0)
            for k in self.__keys:
                self.__channels[k].set_volume(1.0/len(self.__keys))
            self.__activeKeys=self.__keys
            
    
    def generateSounds(self,w,fil=None):
        for k in keyMap:
            f=self.keyFreq(keyMap[k])
            T=1.0/f
            window=1
            if len(w)!=0:
                T=len(w)*self.__Ts
                window=w
            t=np.arange(0,T,self.__Ts)
            
            s=32767.0*np.sin(2*np.pi*f*t)*window
            if fil:
                s=scipy.signal.lfilter(fil[0], fil[1], s)
            self.__channels[k]=pygame.mixer.find_channel(True)
            sound = pygame.sndarray.make_sound(np.int16(s))
            
            self.__channels[k].set_volume(0.0)
            self.__channels[k].play(sound,loops=-1)
            
    def keyFreq(self,n):
        #0 =A=440Hz
        return np.power(2,(n-49)/12)*440#Hz
    def setKeys(self,keys):
        self.__keys=keys
    def diffKeys(self,keys):
        if len(keys)!=len(self.__keys):
            return True
        for k in keys:
            if k not in self.__keys.keys():
                return True
            if keys[k]!=self.__keys[k]:
                return True
        return False
