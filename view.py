'''
Created on Jan 3, 2018

@author: Alexei Figueroa

This module holds the classes related to views in the synthesizer application.
'''
import pygame,abc,CONSTANTS

class View(metaclass=abc.ABCMeta):
    """
    Interface specifiying the method signatures of a View
    """
    def __init__(self, screen):
        self.screen=screen
    @abc.abstractmethod
    def draw(self):
        """
        This method should enable the View to be rendered on
        the screen.
        """


class KeyboardView(View):
    '''
    This class draws the synthesizer keyboard on the screen
    it implements the View interface.
    '''

    def __init__(self, screen):
        '''
        Constructor
        @screen: pygame.display 
            Canvas where the keyboard will be rendered
        '''
        super().__init__(screen)
        self.__pressed={}
    
    def draw(self):
        '''
            This method renders the each key, set's a label for 
            each one of them depending on the state of the View.
        '''
        x0=90
        y0=40
        
        label_font = pygame.font.SysFont("monospace", 15)
        #Render white keys
        for code,k,label,x in CONSTANTS.whites:
            width=20
            height=200
            x_i=10+x*(width+2)+x0
            color_i=CONSTANTS.color_white if code not in self.pressed else CONSTANTS.color_pressed
            pygame.draw.rect(self.screen, color_i, [x_i, y0, width, height])
            k_label = label_font.render(k, 1, CONSTANTS.color_black)
            self.screen.blit(k_label, (x_i+width/3, height-20+y0))
        #Render black keys    
        for code,k,label,x in CONSTANTS.blacks:
            color_i=CONSTANTS.color_black if code not in self.pressed else CONSTANTS.color_pressed
            width=15
            height=130
            x_i=10+(20+2)*x-width/2+x0
            pygame.draw.rect(self.screen, color_i, [x_i, y0, width, height])
            k_label = label_font.render(k, 1, CONSTANTS.color_white)
            self.screen.blit(k_label, (x_i+width/5, height-20+y0))
    """
    Getters and setters, properties
    """
    #Property holding the state of the pressed keys in the View.
    def set_pressed(self,pressed):
        self.__pressed=pressed
    def get_pressed(self):
        return self.__pressed
    pressed=property(get_pressed,set_pressed)

class VibratoView(View):
    """
    This class draws the vibrato control on the screen, it implements
    the View interface
    """
    def __init__(self, screen):
        '''
        Constructor
        @screen: pygame.display 
            Canvas where the vibrato control will be rendered
        '''
        super().__init__(screen)
        self.__vibrato=False
    def draw(self):
        label_font = pygame.font.SysFont("monospace", 15)
        vibrato_state={False:"Toggle vibrato with V (off)",
                       True:"Toggle vibrato with V (on)"}
        vibrato_label = label_font.render(vibrato_state[self.__vibrato], 1, CONSTANTS.color_white)
        pygame.draw.rect(self.screen,CONSTANTS.color_black,[20,280,400,20])
        self.screen.blit(vibrato_label, (20, 280))
    """
    Getters and setters, properties
    """
    #Property holding the state of the vibrato being displayed.    
    def get_vibrato(self):
        return self.__vibrato
    def set_vibrato(self,vibrato):
        self.__vibrato=vibrato
    vibrato=property(get_vibrato,set_vibrato)
    
    