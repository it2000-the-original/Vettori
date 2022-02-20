from Dialogs.YNameDialog import *

class YNameManager(QtWidgets.QDialog):

    def __init__(self, parent):

        # init the class and setuo the window

        super().__init__(parent)
        self.nameWindow = Ui_YName()
        self.nameWindow.setupUi(self)
        self.parent = parent
        self.setFixedSize(self.minimumSize())

        # add a command for the ok button

        self.nameWindow.OkButton.clicked.connect(self.setYName)
    
    def setYName(self):

        self.parent.graphic.setYname(self.nameWindow.NameLine.text(), 
        self.nameWindow.TextSizeLine.value())
        self.close()
        self.parent.ui.statusbar.showMessage(f"YName changed \"{self.nameWindow.NameLine.text()}\"")

    def clear(self):

        # This fuction reset all elements of the window

        self.nameWindow.NameLine.setText(self.parent.graphic.ystringname)
        self.nameWindow.TextSizeLine.setValue(self.parent.graphic.ysize)