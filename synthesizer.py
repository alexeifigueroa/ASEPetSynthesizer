'''
Created on 8 Dec 2017
@author: alexei.figueroa
'''
#conda install -c conda-forge wxpython
import numpy as np
import wave
<<<<<<< HEAD
import io,struct
import wx
import wx.adv
import fractions
import functools
import os
import pygame

=======
import winsound,io,struct
import wx
import wx.adv
from collections import defaultdict
import fractions
import functools
>>>>>>> 97a1d9734520780bcfa5ba4ed594a00d48d6e415
#https://scicomp.stackexchange.com/questions/21230/lcm-builtin-in-python-numpy
def lcm(a,b): 
    return abs(a * b) / fractions.gcd(a,b) if a and b else 0
def keyFreq(n):
    #0 =A0
    return np.power(2,(n-49)/12)*440#Hz
<<<<<<< HEAD
def opj(path):
    """Convert paths to the platform-specific separator"""
    st = os.path.join(*tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    return st

=======
>>>>>>> 97a1d9734520780bcfa5ba4ed594a00d48d6e415
def createSoundFreq(Fs=44100.0,key=49):
    f=keyFreq(key)    #Hz
    T=1/f #1 period
    t=np.arange(0,T,1/Fs)
    s=np.int16(32767.0*3/4*np.cos(2*np.pi*f*t))
    x=struct.pack('<%sh'%s.size,*s)

    memory_file = io.BytesIO()
    with wave.open(memory_file, 'wb') as f :
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(int(Fs))
        f.writeframes(x)
    sound =wx.adv.Sound()
    sound.CreateFromData(memory_file.getvalue())
    
    return sound
    #winsound.PlaySound(memory_file.getvalue(), winsound.SND_MEMORY)

class wxHelloApp(wx.App):
    
    
    def OnInit(self):
        self.__keyMap={65:49,    # A -> A
              87:50,    # W -> A#
              83:51,    # S -> B
              68:52,    # D -> C
              82:53,    # R -> C#
              70:54,    # F -> D
              84:55,    # T -> D#
              71:56,    # G -> E
              72:57,    # H -> F
              85:58,    # U -> F#
              74:59,    # J -> G
              73:60,    # I -> G#
              75:61,    # K -> A
              79:62,    # O -> A#
              76:63,    # L -> B
              246:64    # oe -> C
              }
<<<<<<< HEAD
        
        self.__pressedKey={}
        self.__activesignal=None
        self.__frame = wx.Frame(None, title="ASEPetSynthesizer")
=======
        self.__pressedKey={}
        self.__frame = wx.Frame(None, title="New Stuff")
>>>>>>> 97a1d9734520780bcfa5ba4ed594a00d48d6e415
        self.__frame.Show()
        frameSizer=wx.BoxSizer(wx.VERTICAL)
        yeahButton=wx.Button(self.__frame,label="My button")
        frameSizer.Add(yeahButton)
        yeahButton.Bind(wx.EVT_BUTTON,self.onButtonClicked)
        self.__frame.SetSizer(frameSizer)
        self.SetTopWindow(self.__frame)
        self.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
        self.Bind(wx.EVT_KEY_UP, self.onKeyRelease)
        return True
    def onButtonClicked(self,event):
<<<<<<< HEAD
        Fs=44100
        key=49
        f=keyFreq(key)    #Hz
        T=1/f #1 period
        t=np.arange(0,T,1.0/Fs)
        s=np.int16(32767.0*3/4*np.cos(2*np.pi*f*t))
        pygame.mixer.pre_init(Fs, size=-16, channels=1)
        pygame.mixer.init()
        sound = pygame.sndarray.make_sound(s)
        sound.play(loops=-1)
    def onKeyPress(self,event):
        code=event.GetKeyCode()
        print(code)
        if code in self.__keyMap and code not in self.__pressedKey:
            self.__pressedKey[code]=True
            self.__activesignal=self.createSignals()
            self.__activesignal.play(loops=-1)
            #self.__pressedKey[code].Play(wx.adv.SOUND_ASYNC|wx.adv.SOUND_LOOP)
    def onKeyRelease(self,event):
        code=event.GetKeyCode()
        print("released "+str(code)+" "+str(chr(code)))
        if code in self.__pressedKey:
            #self.__pressedKey[code].Stop()
            self.__pressedKey.pop(code)
            self.__activesignal.stop()
            #self.createSignals()
        #wx.adv.Sound.Stop()
=======
        createSoundFreq(key=49)
    def onKeyPress(self,event):
        code=event.GetKeyCode()
        #print(code)
        if code in self.__keyMap and code not in self.__pressedKey:
            self.__pressedKey[code]=True
            self.createSignals()
            #self.__pressedKey[code].Play(wx.adv.SOUND_ASYNC|wx.adv.SOUND_LOOP)
    def onKeyRelease(self,event):
        code=event.GetKeyCode()
        #print("released "+str(code)+" "+str(chr(code)))
        if code in self.__pressedKey:
            #self.__pressedKey[code].Stop()
            self.__pressedKey.pop(code)
            self.createSignals()
>>>>>>> 97a1d9734520780bcfa5ba4ed594a00d48d6e415
        #dial=wx.MessageDialog(self.__frame,"Here's a dialog")
        #dial.ShowModal()
    def createSignals(self):
        #createSoundFreq(key=self.__keyMap[code])
<<<<<<< HEAD
        Fs=44100  #Sampling frequency
        Ts=1.0/Fs     #Sampling time
        #Find the mcm of the period
        
        T=[1/keyFreq(self.__pressedKey[k])   for k in self.__pressedKey] 
        if len(T)==1:
            T=[T[0],T[0]]
        Tglobal=functools.reduce(lcm,T)
        t=np.arange(0,Tglobal-Ts,Ts)
        Sglobal=np.zeros(int(Tglobal/Ts))
        for k  in self.__pressedKey:
            f=keyFreq(self.__keyMap[k])    #Hz
            s=np.int16(32767.0*1/len(self.__pressedKey)*np.cos(2*np.pi*f*t))
            Sglobal+=s
        pygame.mixer.pre_init(Fs, size=-16, channels=1)
        pygame.mixer.init()
        sound = pygame.sndarray.make_sound(np.int16(Sglobal))
        return sound







if __name__ == "__main__":
    app = wxHelloApp()
    app.MainLoop()
    



=======
        Fs=44100.0
        
        #Find the mcm of the period
        
        T=[1/keyFreq(self.__pressedKey[k])   for k in self.__pressedKey] 
        
        [Tglobal]=functools.reduce(lcm,T)
        Sglobal=np.zeros(int(Tglobal/Fs))
        for k  in self.__pressedKey:
            f=keyFreq(self.__pressedKey[k])    #Hz
            T=1/f #1 period
            t=np.arange(0,T,1/Fs)
            s=np.int16(32767.0*1/len(T)*np.cos(2*np.pi*f*t))
            Sglobal+=s
        x=struct.pack('<%sh'%Sglobal.size,*Sglobal)
        
        memory_file = io.BytesIO()
        with wave.open(memory_file, 'wb') as f :
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(int(Fs))
            f.writeframes(x)
        sound =wx.adv.Sound()
        sound.CreateFromData(memory_file.getvalue())
        sound.Play(wx.adv.SOUND_ASYNC|wx.adv.SOUND_LOOP)   
if __name__ == "__main__":
    app = wxHelloApp()
    app.MainLoop()
>>>>>>> 97a1d9734520780bcfa5ba4ed594a00d48d6e415

