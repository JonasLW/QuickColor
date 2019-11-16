import sys
from krita import *

class QuickColorExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToZero(self):
        #Swaps the foreground color to color nr. 0 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(0).color()
                view.setForeGroundColor(color)
                
     def swapToOne(self):
        #Swaps the foreground color to color nr. 1 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(1).color()
                view.setForeGroundColor(color)

    def swapToTwo(self):
        #Swaps the foreground color to color nr. 2 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(2).color()
                view.setForeGroundColor(color)

    def swapToThree(self):
        #Swaps the foreground color to color nr. 3 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(3).color()
                view.setForeGroundColor(color)
                
    def swapToFour(self):
        #Swaps the foreground color to color nr. 4 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(4).color()
                view.setForeGroundColor(color)
                
    def createActions(self, window):
        action = window.createAction("QuickColor0", "QuickColor0")
        action.triggered.connect(self.swapToZero)
        
        action = window.createAction("QuickColor1", "QuickColor1")
        action.triggered.connect(self.swapToOne)
        
        action = window.createAction("QuickColor2", "QuickColor2")
        action.triggered.connect(self.swapToTwo)
        
        action = window.createAction("QuickColor3", "QuickColor3")
        action.triggered.connect(self.swapToThree)   
        
        action = window.createAction("QuickColor4", "QuickColor4")
        action.triggered.connect(self.swapToFour)
        

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickColorExtension(Krita.instance()))
