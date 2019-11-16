import sys
from krita import *

class QuickWhiteExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToWhite(self):
        #Swaps the foreground color to color nr. 0 in the palette called "Teaching"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "Teaching":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(0).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickWhite", "QuickWhite")
        action.triggered.connect(self.swapToWhite)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickWhiteExtension(Krita.instance()))
