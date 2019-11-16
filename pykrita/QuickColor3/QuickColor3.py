import sys
from krita import *

class QuickThreeExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToThree(self):
        #Swaps the foreground color to color nr. 3 in the palette called "QuickColor"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "QuickColor":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(3).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickColor3", "QuickColor3")
        action.triggered.connect(self.swapToThree)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickThreeExtension(Krita.instance()))
