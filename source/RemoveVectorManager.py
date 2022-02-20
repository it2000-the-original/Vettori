from Dialogs.RemoveVectorDialog import *
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox

class RemoveVectorManager(QtWidgets.QDialog):

    def __init__(self, parent):

        # init the class and setuo the window

        super().__init__(parent)
        self.removeVectorWindow = Ui_RemoveVector()
        self.removeVectorWindow.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.parent = parent
        counter = 1

        # adding the items for every point object in the list

        for l in self.parent.graphic.vettors:

            self.removeVectorWindow.listVectors.addItem(f"{counter} {l.Name}")
            counter += 1

        # add a command for the item doubleclicked

        self.removeVectorWindow.listVectors.itemDoubleClicked.connect(self.ListVectorClicked)

        
    def ListVectorClicked(self, item):

        ret = QMessageBox.question(self, 'Remove a vector', "Are you sure to remove the vector?")
        
        if ret == QMessageBox.Yes:

            self.removeVector(self.removeVectorWindow.listVectors.currentRow())

    def removeVector(self, num):

        name = self.parent.graphic.vettors[num].Name
        self.parent.graphic.removeVector(num)
        self.close()
        self.parent.ui.statusbar.showMessage(f"Vector \"{name}\" deleted!")

    def clear(self):

        # This fuction reset all elements of the window

        self.removeVectorWindow.listVectors.clear()
        counter = 1

        for l in self.parent.graphic.vettors:

            self.removeVectorWindow.listVectors.addItem(f"{counter} {l.Name}")
            counter += 1