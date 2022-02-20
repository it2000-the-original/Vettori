from math import sin, cos, radians
from PyQt5.QtWidgets import QColorDialog, QMessageBox
from Dialogs.ModifyVectorDialog import *

class ModifyVectorManager(QtWidgets.QDialog):

    def __init__(self, parent):

        # init the class and setuo the window

        super().__init__(parent)
        self.modifyVectorWindow = Ui_ModifyVector()
        self.modifyVectorWindow.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.setInclinationMetod()
        self.setAnnotationMetod()
        self.parent = parent
        self.setMetod()

        # connect the correct fuction of every button of the dialog window

        self.modifyVectorWindow.GenerationMetod.currentIndexChanged.connect(self.setMetod)
        self.modifyVectorWindow.InclinationMetod.currentIndexChanged.connect(self.setInclinationMetod)
        self.modifyVectorWindow.AnnonationMetod.currentIndexChanged.connect(self.setAnnotationMetod)
        self.modifyVectorWindow.PathColorButton.clicked.connect(self.openColorDialog)
        self.modifyVectorWindow.OkButton.clicked.connect(self.close)
        self.modifyVectorWindow.ApplyButton.clicked.connect(self.modifyVector)

    def setVector(self, Vet, Nu):

        # setting all variable of the point object

        self.modifyVectorWindow.VectorNameLine.setText(Vet.Name)
        self.modifyVectorWindow.VectorColorLine.setText(Vet.Color)
        self.modifyVectorWindow.point_of_origin_x_Line.setValue(Vet.StartX)
        self.modifyVectorWindow.point_of_origin_y_Line.setValue(Vet.StartY)
        self.modifyVectorWindow.point_of_end_x_Line.setValue(Vet.EndX)
        self.modifyVectorWindow.point_of_end_y_Line.setValue(Vet.EndY)
        self.modifyVectorWindow.VectorSizeLine.setValue(1.0)
        self.modifyVectorWindow.XInclinationLine.setValue(45.0)
        self.modifyVectorWindow.YInclinationLine.setValue(45.0)
        self.number = Nu
        self.annotation = Vet.Annotation
        self.modifyVectorWindow.AnnotationTextLine.setText(Vet.AnnotationText)
        self.modifyVectorWindow.AnnotationXLine.setValue(Vet.AnnotationX)
        self.modifyVectorWindow.AnnotationYLine.setValue(Vet.AnnotationY)

        if self.annotation:

            self.modifyVectorWindow.AnnonationMetod.setCurrentIndex(1)

        else:

            self.modifyVectorWindow.AnnonationMetod.setCurrentIndex(0)

    def setInclinationMetod(self):

        # This fuction change the generation metod with respect to the axis X/Y

        if self.modifyVectorWindow.InclinationMetod.currentText() == "X Inclination":

            self.modifyVectorWindow.XInclinationLine.setEnabled(True)
            self.modifyVectorWindow.YInclinationLine.setEnabled(False)

        else:

            self.modifyVectorWindow.XInclinationLine.setEnabled(False)
            self.modifyVectorWindow.YInclinationLine.setEnabled(True)

    def setMetod(self):

        # this fuction switch the generation metod of the vector,
        # Or with two points or with size and inclination of two axis

        if self.modifyVectorWindow.GenerationMetod.currentText() == "Show size and inclination":
            
            self.modifyVectorWindow.point_of_end_x_Line.setEnabled(False)
            self.modifyVectorWindow.point_of_end_y_Line.setEnabled(False)
            self.modifyVectorWindow.InclinationMetod.setEnabled(True)
            self.setInclinationMetod()
            self.modifyVectorWindow.VectorSizeLine.setEnabled(True)

        else:
            
            self.modifyVectorWindow.point_of_end_x_Line.setEnabled(True)
            self.modifyVectorWindow.point_of_end_y_Line.setEnabled(True)
            self.modifyVectorWindow.InclinationMetod.setEnabled(False)
            self.modifyVectorWindow.XInclinationLine.setEnabled(False)
            self.modifyVectorWindow.YInclinationLine.setEnabled(False)
            self.modifyVectorWindow.VectorSizeLine.setEnabled(False)

    def setAnnotationMetod(self):

        if self.modifyVectorWindow.AnnonationMetod.currentText() == "No Annotation":

            self.modifyVectorWindow.AnnotationTextLine.setEnabled(False)
            self.modifyVectorWindow.AnnotationXLine.setEnabled(False)
            self.modifyVectorWindow.AnnotationYLine.setEnabled(False)
            self.annotation = False

        else:

            self.modifyVectorWindow.AnnotationTextLine.setEnabled(True)
            self.modifyVectorWindow.AnnotationXLine.setEnabled(True)
            self.modifyVectorWindow.AnnotationYLine.setEnabled(True)
            self.annotation = True

    def openColorDialog(self):

        # open a dialog to choose the color of the point

        color = QColorDialog.getColor()
        self.modifyVectorWindow.VectorColorLine.setText(color.name())

    def modifyVector(self):

        if self.parent.theNameAlreadyExistJump(self.modifyVectorWindow.VectorNameLine.text(), self.parent.graphic.vettors, self.number):

            QMessageBox.warning(self, "WARNING", "The name of your vactor already exist")

        else:

            if self.modifyVectorWindow.GenerationMetod.currentText() == "Show points":

                self.parent.graphic.vettors[self.number].Name           = self.modifyVectorWindow.VectorNameLine.text()
                self.parent.graphic.vettors[self.number].Color          = self.modifyVectorWindow.VectorColorLine.text()
                self.parent.graphic.vettors[self.number].StartX         = self.modifyVectorWindow.point_of_origin_x_Line.value()
                self.parent.graphic.vettors[self.number].StartY         = self.modifyVectorWindow.point_of_origin_y_Line.value()
                self.parent.graphic.vettors[self.number].EndX           = self.modifyVectorWindow.point_of_end_x_Line.value()
                self.parent.graphic.vettors[self.number].EndY           = self.modifyVectorWindow.point_of_end_y_Line.value()
                self.parent.graphic.vettors[self.number].Annotation     = self.annotation
                self.parent.graphic.vettors[self.number].AnnotationText = self.modifyVectorWindow.AnnotationTextLine.text()
                self.parent.graphic.vettors[self.number].AnnotationX    = self.modifyVectorWindow.AnnotationXLine.value()
                self.parent.graphic.vettors[self.number].AnnotationY    = self.modifyVectorWindow.AnnotationYLine.value()
                self.parent.graphic.update()

            else:

                if self.modifyVectorWindow.InclinationMetod.currentText() == "X Inclination":

                    XSize = self.modifyVectorWindow.VectorSizeLine.value() * cos(radians(self.modifyVectorWindow.XInclinationLine.value()))
                    YSize = self.modifyVectorWindow.VectorSizeLine.value() * sin(radians(self.modifyVectorWindow.XInclinationLine.value()))
                    self.parent.graphic.vettors[self.number].Name           = self.modifyVectorWindow.VectorNameLine.text()
                    self.parent.graphic.vettors[self.number].Color          = self.modifyVectorWindow.VectorColorLine.text()
                    self.parent.graphic.vettors[self.number].StartX         = self.modifyVectorWindow.point_of_origin_x_Line.value()
                    self.parent.graphic.vettors[self.number].StartY         = self.modifyVectorWindow.point_of_origin_y_Line.value()
                    self.parent.graphic.vettors[self.number].EndX           = self.parent.graphic.vettors[self.number].StartX + XSize
                    self.parent.graphic.vettors[self.number].EndY           = self.parent.graphic.vettors[self.number].StartY + YSize
                    self.parent.graphic.vettors[self.number].Annotation     = self.annotation
                    self.parent.graphic.vettors[self.number].AnnotationText = self.modifyVectorWindow.AnnotationTextLine.text()
                    self.parent.graphic.vettors[self.number].AnnotationX    = self.modifyVectorWindow.AnnotationXLine.value()
                    self.parent.graphic.vettors[self.number].AnnotationY    = self.modifyVectorWindow.AnnotationYLine.value()
                    self.parent.graphic.update()

                else:

                    XSize = self.modifyVectorWindow.VectorSizeLine.value() * sin(radians(self.modifyVectorWindow.YInclinationLine.value()))
                    YSize = self.modifyVectorWindow.VectorSizeLine.value() * cos(radians(self.modifyVectorWindow.YInclinationLine.value()))
                    self.parent.graphic.vettors[self.number].Name           = self.modifyVectorWindow.VectorNameLine.text()
                    self.parent.graphic.vettors[self.number].Color          = self.modifyVectorWindow.VectorColorLine.text()
                    self.parent.graphic.vettors[self.number].StartX         = self.modifyVectorWindow.point_of_origin_x_Line.value()
                    self.parent.graphic.vettors[self.number].StartY         = self.modifyVectorWindow.point_of_origin_y_Line.value()
                    self.parent.graphic.vettors[self.number].EndX           = self.parent.graphic.vettors[self.number].StartX + XSize
                    self.parent.graphic.vettors[self.number].EndY           = self.parent.graphic.vettors[self.number].StartY + YSize
                    self.parent.graphic.vettors[self.number].Annotation     = self.annotation
                    self.parent.graphic.vettors[self.number].AnnotationText = self.modifyVectorWindow.AnnotationTextLine.text()
                    self.parent.graphic.vettors[self.number].AnnotationX    = self.modifyVectorWindow.AnnotationXLine.value()
                    self.parent.graphic.vettors[self.number].AnnotationY    = self.modifyVectorWindow.AnnotationYLine.value()
                    self.parent.graphic.update()
        
        self.parent.ui.statusbar.showMessage(f"Vector \"{self.modifyVectorWindow.VectorNameLine.text()}\" midified!")