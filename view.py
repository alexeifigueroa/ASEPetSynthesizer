'''
Created on Jan 3, 2018

@author: alexei
'''
import pygame
import abc
class view(metaclass=abc.ABCMeta):
    def __init__(self, screen):
        self.screen=screen
    @abc.abstractmethod
    def draw(self):
        """
        This method should enable the view to be rendered on
        the screen.
        """


class keyboardView(view):
    '''
    This class draws the synthesizer keyboard on the screen
    '''

    def __init__(self, screen):
        '''
        Constructor
        '''
        super().__init__(screen)
        self.__pressed={}
    
    def draw(self):
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
        
        label_font = pygame.font.SysFont("monospace", 15)
        
        for code,k,label,x in whites:
            width=20
            height=200
            x_i=10+x*(width+2)+x0
            color_i=color_white if code not in self.pressed else color_pressed
            pygame.draw.rect(self.screen, color_i, [x_i, y0, width, height])
            k_label = label_font.render(k, 1, (0,0,0))
            self.screen.blit(k_label, (x_i+width/3, height-20+y0))
            
        for code,k,label,x in blacks:
            color_i=color_sharp if code not in self.pressed else color_pressed
            width=15
            height=130
            x_i=10+(20+2)*x-width/2+x0
            pygame.draw.rect(self.screen, color_i, [x_i, y0, width, height])
            k_label = label_font.render(k, 1, (255,255,255))
            self.screen.blit(k_label, (x_i+width/5, height-20+y0))
     
    def setPressed(self,pressed):
        self.__pressed=pressed
    def getPressed(self):
        return self.__pressed
    pressed=property(getPressed,setPressed)

class vibratoView(view):
    """
    This class draws the vibrato control on the screen
    """
    def __init__(self, screen):
        super().__init__(screen)
        self.__vibrato=False
    def draw(self):
        label_font = pygame.font.SysFont("monospace", 15)
        vibrato_state={False:"Toggle vibrato with V (off)",
                       True:"Toggle vibrato with V (on)"}
        vibrato_label = label_font.render(vibrato_state[self.__vibrato], 1, (255,255,255))
        pygame.draw.rect(self.screen,(0,0,0),[20,280,400,20])
        self.screen.blit(vibrato_label, (20, 280))
        
    def getVibrato(self):
        return self.__vibrato
    def setVibrato(self,vibrato):
        self.__vibrato=vibrato
    vibrato=property(getVibrato,setVibrato)
    
    