import sys
from krita import *

class QuickBlueExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToBlue(self):
        #Swaps the foreground color to color nr. 4 in the palette called "Teaching"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "Teaching":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(4).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickBlue", "QuickBlue")
        action.triggered.connect(self.swapToBlue)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickBlueExtension(Krita.instance()))