'''
Created on Jan 3, 2018

@author: Alexei Figueroa

This module holds the Presenter classes following the MVP paradigm
of synchronizing user interaction with domain logic.
'''

class Presenter(object):
    """
    Base class specifiying a Presenter 
    """
    def __init__(self,view,model):
        self.view=view
        self.model=model
        

class PianoPresenter(Presenter):
    '''
    Extends Presenter
    
    This class controls the synchronisation of the states
    of both the synthesizer model and the keyboard View
    '''
    def __init__(self,view,model):
        '''
        Constructor
        @View: pianoView object
        @model: model of synthesizerModel
        '''
        super().__init__(view,model)
        self.view.draw()
    def on_press_keys(self,keys):
        """
        This method handles sends the keys being pressed to the signal
        generator for it to adjust the sound played and synchronizes
        the View of the keyboard
        @keys: Dictionary with keys mapping pygame.key_ constants to a boolean
                defining whether each key is pressed
                
        """
        #Update model
        self.model.switch_on_signal_channels(keys)
        #synchronize View
        self.view.pressed=keys
        self.view.draw()
        
class VibratoPresenter(Presenter):
    '''
    Extends Presenter
    
    This class controls the synchronisation of the states
    of both the vibrato model and the vibrato View
    '''
    def __init__(self,view,model):
        '''
        Constructor
        @View: vibratoView object
        @model: model of synthesizerModel
        '''
        super().__init__(view,model)
        view.draw()
        
    def on_toggle_vibrato(self):
        """
        This method handles the switching on and off of the
        windowing function applied to the sine waves in the synthesizer model
        as well as it syncrhonizes the View rendered on the screen.
        """
        #Update model
        self.model.vibrato=not self.model.vibrato
        self.model.initialize_generator()
        #synchronize View
        self.view.vibrato=self.model.vibrato
        self.view.draw()
    