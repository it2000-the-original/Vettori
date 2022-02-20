from Dialogs.GenerateSubtractVectorDialog import *
from PyQt5.QtWidgets import QColorDialog, QListWidgetItem, QMessageBox, QWidget

class GenerateSubtractVectorManager(QtWidgets.QDialog):
    
    def __init__(self, parent):
        
        # init the class and setuo the window

        super().__init__()
        self.generateSubtractVectorWindow = Ui_GenerateSubtractVector()
        self.generateSubtractVectorWindow.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.parent = parent
        self.annotation = False
        self.resetComboBoxes()
        self.setUntitled()
        self.setAnnotationMetod()

        # connect the correct fuction of every button of the dialog window
        
        self.generateSubtractVectorWindow.PathColorButton.clicked.connect(self.openColorDialog)
        self.generateSubtractVectorWindow.GenerateSubtractVectorButton.clicked.connect(self.generateSubtractVector)
        self.generateSubtractVectorWindow.AnnonationMetod.currentIndexChanged.connect(self.setAnnotationMetod)
        
    def resetComboBoxes(self):
        
        # this set all combo boxes in the default option

        self.generateSubtractVectorWindow.ComboFirstVectors.clear()
        self.generateSubtractVectorWindow.ComboSecondVectors.clear()
        n = 1
        
        for i in self.parent.graphic.vettors:
            
            self.generateSubtractVectorWindow.ComboFirstVectors.addItem(f"{n} {i.Name}")
            self.generateSubtractVectorWindow.ComboSecondVectors.addItem(f"{n} {i.Name}")
            n += 1
            
    def setUntitled(self):

        # This check if the name untitle is already in use and
        # if yes it add a number for examle "Untitled1"
        
        UntitledName = "Untitled"
        Result = "Untitled"
        number = 0

        len(Result)

        for n in range(len(self.parent.graphic.vettors)):

            if  self.parent.graphic.vettors[n].Name == Result:
                number += 1
                Result = UntitledName + str(number)
                n = 0

        self.generateSubtractVectorWindow.VectorNameLine.setText(Result)

    def setAnnotationMetod(self):

        if self.generateSubtractVectorWindow.AnnonationMetod.currentText() == "No Annotation":

            self.generateSubtractVectorWindow.AnnotationTextLine.setEnabled(False)
            self.generateSubtractVectorWindow.AnnotationXLine.setEnabled(False)
            self.generateSubtractVectorWindow.AnnotationYLine.setEnabled(False)
            self.annotation = False

        else:

            self.generateSubtractVectorWindow.AnnotationTextLine.setEnabled(True)
            self.generateSubtractVectorWindow.AnnotationXLine.setEnabled(True)
            self.generateSubtractVectorWindow.AnnotationYLine.setEnabled(True)
            self.annotation = True
        
    def openColorDialog(self):

        # This open a dialog to choose the color
        # and after add that color in tha line edit
        
        color = QColorDialog.getColor()
        self.generateSubtractVectorWindow.VectorColorLine.setText(color.name())

    def generateSubtractVector(self):

        if self.parent.theNameAlreadyExist(self.generateSubtractVectorWindow.VectorNameLine.text(), self.parent.graphic.vettors):
            
            QMessageBox.warning(self, "WARNING", "The name of your point already exist")

        else:

            self.parent.graphic.generateSubtractVector(

                self.generateSubtractVectorWindow.VectorNameLine.text(),
                self.generateSubtractVectorWindow.point_of_origin_x_Line.value(),
                self.generateSubtractVectorWindow.point_of_origin_y_Line.value(),
                self.generateSubtractVectorWindow.ComboFirstVectors.currentIndex(),
                self.generateSubtractVectorWindow.ComboSecondVectors.currentIndex(),
                self.generateSubtractVectorWindow.VectorColorLine.text(),
                self.annotation,
                self.generateSubtractVectorWindow.AnnotationTextLine.text(),
                self.generateSubtractVectorWindow.AnnotationXLine.value(),
                self.generateSubtractVectorWindow.AnnotationYLine.value()
            )

            self.close()
            self.parent.ui.statusbar.showMessage(f"New vector \"{self.generateSubtractVectorWindow.VectorNameLine.text()}\" added!")
        
    def clear(self):

        # This fuction reset all elements of the window
        
        self.generateSubtractVectorWindow.VectorColorLine.setText("#000000")
        self.generateSubtractVectorWindow.point_of_origin_x_Line.setValue(0)
        self.generateSubtractVectorWindow.point_of_origin_y_Line.setValue(0)
        self.setUntitled()
        self.resetComboBoxes()