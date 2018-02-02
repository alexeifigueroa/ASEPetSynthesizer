'''
Created on Jan 3, 2018

@author: Alexei Figueroa

This module holds the presenter classes following the MVP paradigm
of synchronizing user interaction with domain logic.
'''

class presenter(object):
    """
    Base class specifiying a presenter 
    """
    def __init__(self,view,model):
        self.view=view
        self.model=model
        

class pianoPresenter(presenter):
    '''
    Extends presenter
    
    This class controls the synchronisation of the states
    of both the synthesizer model and the keyboard view
    '''
    def __init__(self,view,model):
        '''
        Constructor
        @view: pianoView object
        @model: model of synthesizerModel
        '''
        super().__init__(view,model)
        self.view.draw()
    def onPressKeys(self,keys):
        """
        This method handles sends the keys being pressed to the signal
        generator for it to adjust the sound played and synchronizes
        the view of the keyboard
        @keys: Dictionary with keys mapping pygame.key_ constants to a boolean
                defining whether each key is pressed
                
        """
        #Update model
        self.model.switchOnSignalChannels(keys)
        #synchronize view
        self.view.pressed=keys
        self.view.draw()
        
class vibratoPresenter(presenter):
    '''
    Extends presenter
    
    This class controls the synchronisation of the states
    of both the vibrato model and the vibrato view
    '''
    def __init__(self,view,model):
        '''
        Constructor
        @view: vibratoView object
        @model: model of synthesizerModel
        '''
        super().__init__(view,model)
        view.draw()
        
    def onToggleVibrato(self):
        """
        This method handles the switching on and off of the
        windowing function applied to the sine waves in the synthesizer model
        as well as it syncrhonizes the view rendered on the screen.
        """
        #Update model
        self.model.vibrato=not self.model.vibrato
        self.model.initializeGenerator()
        #synchronize view
        self.view.vibrato=self.model.vibrato
        self.view.draw()
    