import sys
from krita import *

class QuickColorExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swap(self, index):
        #Swaps the foreground color to a color from the palette called "QuickColor", by index
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(index).color()
                view.setForeGroundColor(color)
                
    def createActions(self, window):
        action = window.createAction("QuickColor0", "QuickColor0")
        action.triggered.connect(self.swap(0))
        
        action = window.createAction("QuickColor1", "QuickColor1")
        action.triggered.connect(self.swap(1))
        
        action = window.createAction("QuickColor2", "QuickColor2")
        action.triggered.connect(self.swap(2))
        
        action = window.createAction("QuickColor3", "QuickColor3")
        action.triggered.connect(self.swap(3))   
        
        action = window.createAction("QuickColor4", "QuickColor4")
        action.triggered.connect(self.swap(4))
        

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickColorExtension(Krita.instance()))
