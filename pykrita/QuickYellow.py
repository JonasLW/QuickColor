import sys
from krita import *

class QuickYellowExtension(Extension):

    def __init__(self, parent):
        #Initialising the parent, important when subclassing
        super().__init__(parent)

    def setup(self):
        pass

    def swapToYellow(self):
        #Swaps the foreground color to color nr. 6 in the palette called "Teaching"
        resources = Application.resources("palette")
        view = Krita.instance().activeWindow().activeView()
        for (name, item) in resources.items():
            if name == "Teaching":
                palette = Palette(item)
                color = palette.colorSetEntryByIndex(6).color()
                view.setForeGroundColor(color)

    def createActions(self, window):
        action = window.createAction("QuickYellow", "QuickYellow")
        action.triggered.connect(self.swapToYellow)

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickYellowExtension(Krita.instance()))