import sys
from krita import *

class QuickRedExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToRed(self):
        #Swaps the foreground color to color nr. 5 in the palette called "Teaching"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "Teaching":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(5).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickRed", "QuickRed")
        action.triggered.connect(self.swapToRed)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickRedExtension(Krita.instance()))