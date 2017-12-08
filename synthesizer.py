'''
Created on 8 Dec 2017
@author: alexei.figueroa
'''
#conda install -c conda-forge wxpython
import numpy as np
import wave
import winsound,io,struct
import wx
import wx.adv
from collections import defaultdict
import fractions
import functools
#https://scicomp.stackexchange.com/questions/21230/lcm-builtin-in-python-numpy
def lcm(a,b): 
    return abs(a * b) / fractions.gcd(a,b) if a and b else 0
def keyFreq(n):
    #0 =A0
    return np.power(2,(n-49)/12)*440#Hz
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
        self.__pressedKey={}
        self.__frame = wx.Frame(None, title="New Stuff")
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
        #dial=wx.MessageDialog(self.__frame,"Here's a dialog")
        #dial.ShowModal()
    def createSignals(self):
        #createSoundFreq(key=self.__keyMap[code])
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

