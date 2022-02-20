from Dialogs.RemovePointDialog import *
from PyQt5.QtWidgets import QMessageBox

class RemovePointManager(QtWidgets.QDialog):

    def __init__(self, parent):

        # init the class and setuo the window

        super().__init__(parent)
        self.removePointWindow = Ui_RemovePoint()
        self.removePointWindow.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.parent = parent
        counter = 1

        # adding the items for every point object in the list

        for l in self.parent.graphic.points:

            self.removePointWindow.listPoints.addItem(f"{counter} {l.Name}")
            counter += 1
            
        # add a command for the item doubleclicked

        self.removePointWindow.listPoints.itemDoubleClicked.connect(self.ListPointClicked)
            
    def ListPointClicked(self, item):

        ret = QMessageBox.question(self, 'Remove a vector', "Are you sure to remove the point?")
        
        if ret == QMessageBox.Yes:

            self.removePoint(self.removePointWindow.listPoints.currentRow())

    def removePoint(self, num):

        name = self.parent.graphic.points[num].Name
        self.parent.graphic.removePoint(num)
        self.close()
        self.parent.ui.statusbar.showMessage(f"Point \"{name}\" deleted!")
            
    def clear(self):

        # This fuction reset all elements of the window

        self.removePointWindow.listPoints.clear()
        counter = 1

        for l in self.parent.graphic.points:

            self.removePointWindow.listPoints.addItem(f"{counter} {l.Name}")
            counter += 1