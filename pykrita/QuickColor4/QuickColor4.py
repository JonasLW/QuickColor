import sys
from krita import *

class QuickFourExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

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
        action = window.createAction("QuickColor4", "QuickColor4")
        action.triggered.connect(self.swapToFour)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickFourExtension(Krita.instance()))
