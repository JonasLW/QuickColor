import sys
from krita import *

class QuickGreenExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToGreen(self):
        #Swaps the foreground color to color nr. 7 in the palette called "Teaching"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "Teaching":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(7).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickGreen", "QuickGreen")
        action.triggered.connect(self.swapToGreen)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickGreenExtension(Krita.instance()))