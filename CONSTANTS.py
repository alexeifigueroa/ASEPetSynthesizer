'''
Created on 2 Feb 2018

@author: Alexei Figueroa

This module holds the constants to be used in the program.

'''
import pygame
#Map of key codes to the number of each key in a keyboard
keyMap={pygame.K_a:49,    # A -> A
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
#lists with the white keys of the keyboard.
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
color_black=(0,0,0)