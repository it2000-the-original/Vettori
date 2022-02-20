from PyQt5.QtWidgets import QColorDialog, QMessageBox
from Dialogs.AddPointDialog import *

class AddPointManager(QtWidgets.QDialog):
    
    def __init__(self, parent):
        
        # init the class and setup the window

        super().__init__(parent)
        self.addPointWindow = Ui_AddPoint()
        self.addPointWindow.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.parent = parent
        self.annotation = False
        self.setUntitled()
        self.setAnnotationMetod()
        
        # connect every button to the righ fuction

        self.addPointWindow.AddPointButton.clicked.connect(self.addPoint)
        self.addPointWindow.PathColorButton.clicked.connect(self.openColorDialog)
        self.addPointWindow.AnnonationMetod.currentIndexChanged.connect(self.setAnnotationMetod)
    
    def setUntitled(self):

        # This check if the name untitle is already in use and
        # if yes it add a number for examle "Untitled1"
        
        UntitledName = "Untitled"
        Result = "Untitled"
        number = 0

        len(Result)

        for n in range(len(self.parent.graphic.points)):

            if  self.parent.graphic.points[n].Name == Result:
                number += 1
                Result = UntitledName + str(number)
                n = 0

        self.addPointWindow.PointNameLine.setText(Result)

    def setAnnotationMetod(self):

        if self.addPointWindow.AnnonationMetod.currentText() == "No Annotation":

            self.addPointWindow.AnnotationTextLine.setEnabled(False)
            self.addPointWindow.AnnotationXLine.setEnabled(False)
            self.addPointWindow.AnnotationYLine.setEnabled(False)
            self.annotation = False

        else:

            self.addPointWindow.AnnotationTextLine.setEnabled(True)
            self.addPointWindow.AnnotationXLine.setEnabled(True)
            self.addPointWindow.AnnotationYLine.setEnabled(True)
            self.annotation = True
        
    def openColorDialog(self):

        # This open a dialog to choose the color
        # and after add that color in tha line edit

        color = QColorDialog.getColor()
        self.addPointWindow.PointColorLine.setText(color.name())

    def addPoint(self):
        
        if self.parent.theNameAlreadyExist(self.addPointWindow.PointNameLine.text(), self.parent.graphic.points):
            
            QMessageBox.warning(self, "WARNING", "The name of your point already exist")
            
        else:
        
            self.parent.graphic.addPoint(
                
                self.addPointWindow.PointNameLine.text(),
                self.addPointWindow.PointXLine.value(),
                self.addPointWindow.PointYLine.value(),
                self.addPointWindow.SizeLine.value(),
                self.addPointWindow.PointColorLine.text(),
                self.annotation,
                self.addPointWindow.AnnotationTextLine.text(),
                self.addPointWindow.AnnotationXLine.value(),
                self.addPointWindow.AnnotationYLine.value()
            )
            
            self.close()
            self.parent.ui.statusbar.showMessage(f"New point \"{self.addPointWindow.PointNameLine.text()}\" added!")
        
    def clear(self):
        
        # This fuction reset all elements of the window

        self.addPointWindow.PointXLine.setProperty("value", 0.0)
        self.addPointWindow.PointYLine.setProperty("value", 0.0)
        self.addPointWindow.SizeLine.setProperty("value", 50.0)
        self.addPointWindow.PointColorLine.setText("#000000")
        self.addPointWindow.AnnotationTextLine.setText("Annotation Text")
        self.addPointWindow.AnnotationXLine.setValue(0.0)
        self.addPointWindow.AnnotationYLine.setValue(0.0)
        self.setUntitled()