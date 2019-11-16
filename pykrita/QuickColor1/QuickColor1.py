import sys
from krita import *

class QuickOneExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToOne(self):
        #Swaps the foreground color to color nr. 1 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(4).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickColor1", "QuickColor1")
        action.triggered.connect(self.swapToOne)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickOneExtension(Krita.instance()))
