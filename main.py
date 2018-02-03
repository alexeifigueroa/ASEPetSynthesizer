'''
Created on Dec 10, 2017

@author: Alexei Figueroa

This file runs the main program, it initializes the pygame mixer and
spawns the Models, Views and Presenters of the synthesizer game and finally
it starts the main event loop.

'''

import pygame
import CONSTANTS
from  view import KeyboardView,VibratoView
from presenter import PianoPresenter,VibratoPresenter
from  model import SynthesizerModel
def main():
    #Initialize pygame and the mixer        
    pygame.mixer.pre_init(44100,-16, 1,1024)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(15)
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    
    done = False
    #Spawn Views, Model and Presenters
    piano=KeyboardView(screen)
    vibrato=VibratoView(screen)
    model=SynthesizerModel()
    keyboard_presenter=PianoPresenter(piano,model)
    vib_presenter=VibratoPresenter(vibrato,model)
    
    #Main event loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type in (pygame.KEYDOWN,pygame.KEYUP) and event.key in CONSTANTS.keyMap:
                pressed = pygame.key.get_pressed()
                keys={i:True for i in range(len(pressed)-1) if pressed[i]==1 and i in CONSTANTS.keyMap}
                keyboard_presenter.on_press_keys(keys)
            if event.type ==pygame.KEYUP and event.key==pygame.K_v:
                vib_presenter.on_toggle_vibrato()
        pygame.display.flip()
            
if __name__ == "__main__":
    main()
        