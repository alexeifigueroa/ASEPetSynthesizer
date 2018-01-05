'''
Created on Jan 3, 2018

@author: alexei
'''

class presenter(object):
    def __init__(self,view,model):
        self.view=view
        self.model=model
        

class pianoPresenter(presenter):
    '''
    classdocs
    '''
    def __init__(self,view,model):
        '''
        Constructor
        '''
        super().__init__(view,model)
        view.draw()
    def onPressKeys(self,keys):
        #Update model
        self.model.switchOnSignalChannels(keys)
        #synchronize view
        self.view.pressed=keys
        self.view.draw()
        
class vibratoPresenter(presenter):
    def __init__(self,view,model):
        super().__init__(view,model)
        view.draw()
        
    def onToggleVibrato(self):
        #Update model
        self.model.vibrato=not self.model.vibrato
        self.model.initializeGenerator()
        #synchronize view
        self.view.vibrato=self.model.vibrato
        self.view.draw()
    