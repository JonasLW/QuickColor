import sys
from krita import *

class QuickZeroExtension(Extension):

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

    def createActions(self, window):
        action = window.createAction("QuickColor0", "QuickColor0")
        action.triggered.connect(self.swapToZero)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickZeroExtension(Krita.instance()))
