from krita import *
import functools
from PyQt5.QtWidgets import QErrorMessage

class QuickColorExtension(Extension):

    def __init__(self, parent, paletteName):
        #Initialising the parent, important when subclassing
        super().__init__(parent)
        self.paletteName = paletteName

    def setup(self):
        pass

    def swap(self, index):
        #Swaps the foreground color to a color from the palette called self.paletteName, by index
        view = Krita.instance().activeWindow().activeView()
        resources = Application.resources("palette")
        res = resources.get(self.paletteName, None)
        if res is None:
            em = QErrorMessage()
            em.showMessage("You need a palette named \"" + self.paletteName + "\" for the QuickColorExtension to work")
            em.exec_()
        else:
            palette = Palette(res)
            color = palette.colorSetEntryByIndex(index).color()
            view.setForeGroundColor(color)

    def createActions(self, window):
        for n in range(5):
            name = "QuickColor" + str(n)
            action = window.createAction(name, name)
            action.triggered.connect(functools.partial(self.swap, n))

#Adding extension to Krita's list of extensions
Krita.instance().addExtension(QuickColorExtension(Krita.instance(), "QuickColor"))
