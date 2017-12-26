'''
Created on Dec 10, 2017

@author: alexei
'''

import pygame
import SignalGenerator

def drawPiano(pressed,screen,vibrato):
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
    x0=90
    y0=40
    
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    label_font = pygame.font.SysFont("monospace", 15)

    # render text
    
    for code,k,label,x in whites:
        width=20
        height=200
        x_i=10+x*(width+2)+x0
        color_i=color_white if code not in pressed else color_pressed
        pygame.draw.rect(screen, color_i, [x_i, y0, width, height])
        k_label = label_font.render(k, 1, (0,0,0))
        screen.blit(k_label, (x_i+width/3, height-20+y0))
        
    for code,k,label,x in blacks:
        color_i=color_sharp if code not in pressed else color_pressed
        width=15
        height=130
        x_i=10+(20+2)*x-width/2+x0
        pygame.draw.rect(screen, color_i, [x_i, y0, width, height])
        k_label = label_font.render(k, 1, (255,255,255))
        screen.blit(k_label, (x_i+width/5, height-20+y0))
    vibrato_state={False:"Toggle vibrato with V (off)",
                   True:"Toggle vibrato with V (on)"}
    vibrato_label = label_font.render(vibrato_state[vibrato], 1, (255,255,255))
    pygame.draw.rect(screen,(0,0,0),[20,280,400,20])
    screen.blit(vibrato_label, (20, 280))

def main():
            
    pygame.mixer.pre_init(44100,-16, 1,1024)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(15)
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    done = False
    vibrato=False
    drawPiano({},screen,vibrato)
    keys={}
    signalGen=SignalGenerator.SignalGenerator()
    while not done:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
            if event.type in (pygame.KEYDOWN,pygame.KEYUP) and event.key in SignalGenerator.keyMap:
                pressed = pygame.key.get_pressed()
                keys={i:True for i in range(len(pressed)-1) if pressed[i]==1 and i in SignalGenerator.keyMap}
                drawPiano(keys,screen,vibrato)
                signalGen.setKeys(keys)
                signalGen.generate()
            if event.type ==pygame.KEYUP and event.key==pygame.K_v:
                vibrato=not vibrato
                drawPiano(keys,screen,vibrato)
                signalGen=SignalGenerator.SignalGenerator(vibrato)
        pygame.display.flip()
            
if __name__ == "__main__":
    main()
        