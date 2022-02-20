from Dialogs.GenerateSumVectorDialog import *
from PyQt5.QtWidgets import QColorDialog, QListWidgetItem, QMessageBox, QWidget

class GenerateSumVectorManager(QtWidgets.QDialog):
    
    def __init__(self, parent):
        
        # init the class and setuo the window

        super().__init__(parent)
        self.generateSumVectorWindow = Ui_GenerateSumVector()
        self.generateSumVectorWindow.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.parent = parent
        self.annotation = False
        self.resetComboBoxes()
        self.setUntitled()
        self.setAnnotationMetod()

        # connect the correct fuction of every button of the dialog window
        
        self.generateSumVectorWindow.PathColorButton.clicked.connect(self.openColorDialog)
        self.generateSumVectorWindow.GenerateSumVectorButton.clicked.connect(self.generateSumVector)
        self.generateSumVectorWindow.AnnonationMetod.currentIndexChanged.connect(self.setAnnotationMetod)
        
    def resetComboBoxes(self):
        
        # this set all combo boxes in the default option

        self.generateSumVectorWindow.ComboFirstVectors.clear()
        self.generateSumVectorWindow.ComboSecondVectors.clear()
        n = 1
        
        for i in self.parent.graphic.vettors:
            
            self.generateSumVectorWindow.ComboFirstVectors.addItem(f"{n} {i.Name}")
            self.generateSumVectorWindow.ComboSecondVectors.addItem(f"{n} {i.Name}")
            n += 1

    def setAnnotationMetod(self):

        if self.generateSumVectorWindow.AnnonationMetod.currentText() == "No Annotation":

            self.generateSumVectorWindow.AnnotationTextLine.setEnabled(False)
            self.generateSumVectorWindow.AnnotationXLine.setEnabled(False)
            self.generateSumVectorWindow.AnnotationYLine.setEnabled(False)
            self.annotation = False

        else:

            self.generateSumVectorWindow.AnnotationTextLine.setEnabled(True)
            self.generateSumVectorWindow.AnnotationXLine.setEnabled(True)
            self.generateSumVectorWindow.AnnotationYLine.setEnabled(True)
            self.annotation = True
            
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

        self.generateSumVectorWindow.VectorNameLine.setText(Result)
        
    def openColorDialog(self):

        # This open a dialog to choose the color
        # and after add that color in tha line edit
        
        color = QColorDialog.getColor()
        self.generateSumVectorWindow.VectorColorLine.setText(color.name())

    def generateSumVector(self):
        
        if self.parent.theNameAlreadyExist(self.generateSumVectorWindow.VectorNameLine.text(), self.parent.graphic.vettors):
            
            QMessageBox.warning(self, "WARNING", "The name of your point already exist")

        else:

            self.parent.graphic.generateSumVector(
                
                self.generateSumVectorWindow.VectorNameLine.text(),
                self.generateSumVectorWindow.point_of_origin_x_Line.value(),
                self.generateSumVectorWindow.point_of_origin_y_Line.value(),
                self.generateSumVectorWindow.ComboFirstVectors.currentIndex(),
                self.generateSumVectorWindow.ComboSecondVectors.currentIndex(),
                self.generateSumVectorWindow.VectorColorLine.text(),
                self.annotation,
                self.generateSumVectorWindow.AnnotationTextLine.text(),
                self.generateSumVectorWindow.AnnotationXLine.value(),
                self.generateSumVectorWindow.AnnotationYLine.value()
            )
            
            self.close()
            self.parent.ui.statusbar.showMessage(f"New vector \"{self.generateSumVectorWindow.VectorNameLine.text()}\" added!")
        
    def clear(self):

        # This fuction reset all elements of the window
        
        self.generateSumVectorWindow.VectorColorLine.setText("#000000")
        self.generateSumVectorWindow.point_of_origin_x_Line.setValue(0)
        self.generateSumVectorWindow.point_of_origin_y_Line.setValue(0)
        self.setUntitled()
        self.resetComboBoxes()