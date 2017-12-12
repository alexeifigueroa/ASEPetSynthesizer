'''
Created on Dec 10, 2017

@author: alexei
'''

import pygame
import numpy as np
import fractions,functools
from collections import defaultdict
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
sounds=defaultdict(pygame.mixer.Sound)
def keyFreq(n):
    #0 =A=440Hz
    return np.power(2,(n-49)/12)*440#Hz
def drawPiano(pressed):
    whites=[(pygame.K_a,"A","A",0),(pygame.K_s,"S","B",1),
            (pygame.K_d,"D","C",2),(pygame.K_f,"F","D",3),
            (pygame.K_g,"G","E",4),(pygame.K_h,"H","F",5),
            (pygame.K_j,"J","G",6),(pygame.K_k,"K","A",7),
            (pygame.K_l,"L","B",8)]
    blacks=[(pygame.K_w,"W","A#",1),(pygame.K_r,"R","C#",3),
            (pygame.K_t,"T","D#",4),(pygame.K_u,"U","F#",6),
            (pygame.K_i,"I","G#",7),(pygame.K_o,"O","A#",8)]
    color_white=(255,255,255)
    color_pressed=(128,128,128)
    color_sharp=(0,0,0)
    #draw keys
    
    
    for code,k,label,x in whites:
        keyWidth=20
        keyHeight=200
        keyX=10+x*(keyWidth+2)
        keyColor=color_white if code not in pressed else color_pressed
        pygame.draw.rect(screen, keyColor, [keyX, 10, keyWidth, keyHeight])
    for code,k,label,x in blacks:
        keyColor=color_sharp if code not in pressed else color_pressed
        keyWidth=15
        keyHeight=130
        keyX=10+(20+2)*x-keyWidth/2
        pygame.draw.rect(screen, keyColor, [keyX, 10, keyWidth, keyHeight])
def createSounds():
    Fs=44100  #Sampling frequency
    Ts=1.0/Fs #Sampling time
           
    for k in keyMap:
        f=keyFreq(keyMap[k])
        T=1/f #Seconds
        t=np.arange(0,T-Ts,Ts)
        s=np.int16(32767.0*np.cos(2*np.pi*f*t))
        sounds[k]=pygame.sndarray.make_sound(s)
        
pygame.mixer.pre_init(44100, size=-16, channels=1)
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
createSounds()
drawPiano({})
while not done:
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type==pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()
                    keys={i:True for i in range(len(pressed)-1) if pressed[i]==1 and i in keyMap}
                    #print(keys)
                    for k in keys:
                        sounds[k].play(loops=-1)
                    drawPiano(keys)
                if event.type==pygame.KEYUP and event.key in keyMap:
                    sounds[event.key].stop()
                    pressed = pygame.key.get_pressed()
                    keys={i:True for i in range(len(pressed)-1) if pressed[i]==1 and i in keyMap}
                    drawPiano(keys)
                    
        
        pygame.display.flip()