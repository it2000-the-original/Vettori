from PyQt5.QtWidgets import QColorDialog, QMessageBox
from Dialogs.AddVectorDialog import *


class AddVectorManager(QtWidgets.QDialog):

    def __init__(self, parent):
        
        # init the class and setup the window

        super().__init__(parent)
        self.addVectorWindow = Ui_AddVector()
        self.addVectorWindow.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.parent = parent
        self.annotation = False
        self.setUntitled()
        self.setMetod()
        self.setAnnotationMetod()

        # connect the correct fuction of every button of the dialog window

        self.addVectorWindow.AddVectorButton.clicked.connect(self.addVector)
        self.addVectorWindow.GenerationMetod.currentIndexChanged.connect(self.setMetod)
        self.addVectorWindow.InclinationMetod.currentIndexChanged.connect(self.setInclinationMetod)
        self.addVectorWindow.AnnonationMetod.currentIndexChanged.connect(self.setAnnotationMetod)
        self.addVectorWindow.PathColorButton.clicked.connect(self.openColorDialog)
    
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

        self.addVectorWindow.VectorNameLine.setText(Result)

    def openColorDialog(self):

        # This open a dialog to choose the color
        # and after add that color in tha line edit

        color = QColorDialog.getColor()
        self.addVectorWindow.VectorColorLine.setText(color.name())
    
    def setInclinationMetod(self):

        # This fuction change the generation metod with respect to the axis X/Y

        if self.addVectorWindow.InclinationMetod.currentText() == "X Inclination":

            self.addVectorWindow.XInclinationLine.setEnabled(True)
            self.addVectorWindow.YInclinationLine.setEnabled(False)

        else:

            self.addVectorWindow.XInclinationLine.setEnabled(False)
            self.addVectorWindow.YInclinationLine.setEnabled(True)

    def setMetod(self):

        # this fuction switch the generation metod of the vector,
        # Or with two points or with size and inclination of two axis

        if self.addVectorWindow.GenerationMetod.currentText() == "Generate with size and inclination":
            
            self.addVectorWindow.point_of_end_x_Line.setEnabled(False)
            self.addVectorWindow.point_of_end_y_Line.setEnabled(False)
            self.addVectorWindow.InclinationMetod.setEnabled(True)
            self.setInclinationMetod()
            self.addVectorWindow.VectorSizeLine.setEnabled(True)

        else:
            
            self.addVectorWindow.point_of_end_x_Line.setEnabled(True)
            self.addVectorWindow.point_of_end_y_Line.setEnabled(True)
            self.addVectorWindow.InclinationMetod.setEnabled(False)
            self.addVectorWindow.XInclinationLine.setEnabled(False)
            self.addVectorWindow.YInclinationLine.setEnabled(False)
            self.addVectorWindow.VectorSizeLine.setEnabled(False)

    def setAnnotationMetod(self):
        
        # this fuction check if yuo want to create an annotation for your object

        if self.addVectorWindow.AnnonationMetod.currentText() == "No Annotation":

            self.addVectorWindow.AnnotationTextLine.setEnabled(False)
            self.addVectorWindow.AnnotationXLine.setEnabled(False)
            self.addVectorWindow.AnnotationYLine.setEnabled(False)
            self.annotation = False

        else:

            self.addVectorWindow.AnnotationTextLine.setEnabled(True)
            self.addVectorWindow.AnnotationXLine.setEnabled(True)
            self.addVectorWindow.AnnotationYLine.setEnabled(True)
            self.annotation = True

    def addVector(self):
        
        if self.parent.theNameAlreadyExist(self.addVectorWindow.VectorNameLine.text(), self.parent.graphic.vettors):
            
            QMessageBox.warning(self, "WARNING", "The name of your vector already exist")
            
        else:
        
            if self.addVectorWindow.GenerationMetod.currentText() == "Generate with points":
            
                self.parent.graphic.addVector(
                    
                    self.addVectorWindow.VectorNameLine.text(),
                    self.addVectorWindow.point_of_origin_x_Line.value(),
                    self.addVectorWindow.point_of_origin_y_Line.value(),
                    self.addVectorWindow.point_of_end_x_Line.value(),
                    self.addVectorWindow.point_of_end_y_Line.value(),
                    self.addVectorWindow.VectorColorLine.text(),
                    self.annotation,
                    self.addVectorWindow.AnnotationTextLine.text(),
                    self.addVectorWindow.AnnotationXLine.value(),
                    self.addVectorWindow.AnnotationYLine.value()
                )
                
            else:
                
                if self.addVectorWindow.InclinationMetod.currentText() == "X Inclination":
                
                    self.graphic.addVectorWithInclination(
                        
                        self.addVectorWindow.VectorNameLine.text(),
                        self.addVectorWindow.point_of_origin_x_Line.value(),
                        self.addVectorWindow.point_of_origin_y_Line.value(),
                        self.addVectorWindow.VectorSizeLine.value(),
                        self.addVectorWindow.XInclinationLine.value(),
                        "x", self.addVectorWindow.VectorColorLine.text(),
                        self.annotation,
                        self.addVectorWindow.AnnotationTextLine.text(),
                        self.addVectorWindow.AnnotationXLine.value(),
                        self.addVectorWindow.AnnotationYLine.value()
                    )
                    
                else:

                    self.parent.graphic.addVectorWithInclination(
                        
                        self.addVectorWindow.VectorNameLine.text(),
                        self.addVectorWindow.point_of_origin_x_Line.value(),
                        self.addVectorWindow.point_of_origin_y_Line.value(),
                        self.addVectorWindow.VectorSizeLine.value(),
                        self.addVectorWindow.YInclinationLine.value(),
                        "y", self.addVectorWindow.VectorColorLine.text(),
                        self.annotation,
                        self.addVectorWindow.AnnotationTextLine.text(),
                        self.addVectorWindow.AnnotationXLine.value(),
                        self.addVectorWindow.AnnotationYLine.value()
                    )

            self.close()
            self.parent.ui.statusbar.showMessage(f"New vector \"{self.addVectorWindow.VectorNameLine.text()}\" added!")

    def clear(self):

        # This fuction reset all elements of the window

        self.addVectorWindow.point_of_end_x_Line.setProperty("value", 1.0)
        self.addVectorWindow.point_of_end_y_Line.setProperty("value", 1.0)
        self.addVectorWindow.point_of_origin_x_Line.setProperty("value", 0.0)
        self.addVectorWindow.point_of_origin_y_Line.setProperty("value", 0.0)
        self.addVectorWindow.VectorSizeLine.setProperty("value", 1.0)
        self.addVectorWindow.XInclinationLine.setProperty("value", 45.0)
        self.addVectorWindow.YInclinationLine.setProperty("value", 45.0)
        self.addVectorWindow.VectorColorLine.setText("#000000")
        self.addVectorWindow.AnnotationTextLine.setText("Annotation Text")
        self.addVectorWindow.AnnotationXLine.setValue(0.0)
        self.addVectorWindow.AnnotationYLine.setValue(0.0)
        self.setUntitled()