from Dialogs.XNameDialog import *

class XNameManager(QtWidgets.QDialog):

    def __init__(self, parent):

        # init the class and setuo the window

        super().__init__(parent)
        self.nameWindow = Ui_XName()
        self.nameWindow.setupUi(self)
        self.parent = parent
        self.setFixedSize(self.minimumSize())

        # add a command for the ok button

        self.nameWindow.OkButton.clicked.connect(self.setXName)
    
    def setXName(self):

        self.parent.graphic.setXname(self.nameWindow.NameLine.text(),
        self.nameWindow.TextSizeLine.value())
        self.close()
        self.parent.ui.statusbar.showMessage(f"XName changed \"{self.nameWindow.NameLine.text()}\"")

    def clear(self):

        # This fuction reset all elements of the window

        self.nameWindow.NameLine.setText(self.parent.graphic.xstringname)
        self.nameWindow.TextSizeLine.setValue(self.parent.graphic.xsize)