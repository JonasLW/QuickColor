import sys
from krita import *

class QuickTwoExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToTwo(self):
        #Swaps the foreground color to color nr. 2 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(2).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickColor2", "QuickColor2")
        action.triggered.connect(self.swapToTwo)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickTwoExtension(Krita.instance()))
