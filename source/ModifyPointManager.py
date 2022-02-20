from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QColorDialog, QMessageBox
from Dialogs.ModifyPointDialog import *

class ModifyPointManager(QtWidgets.QDialog):

    def __init__(self, parent):

        # init the class and setuo the window

        super().__init__(parent)
        self.modifyPointWindow = Ui_ModifyPoint()
        self.setFixedSize(self.minimumSize())
        self.modifyPointWindow.setupUi(self)
        self.setAnnotationMetod()
        self.parent = parent

        # connect the correct fuction of every button of the dialog window

        self.modifyPointWindow.PathColorButton.clicked.connect(self.openColorDialog)
        self.modifyPointWindow.OkButton.clicked.connect(self.close)
        self.modifyPointWindow.ApplyButton.clicked.connect(self.modifyPoint)
        self.modifyPointWindow.AnnonationMetod.currentIndexChanged.connect(self.setAnnotationMetod)

    def setPoint(self, Poi, Nu):

        # setting all variable of the point object

        self.modifyPointWindow.PointNameLine.setText(Poi.Name)
        self.modifyPointWindow.PointColorLine.setText(Poi.Color)
        self.modifyPointWindow.PointXLine.setValue(Poi.PointX)
        self.modifyPointWindow.PointYLine.setValue(Poi.PointY)
        self.modifyPointWindow.PointSizeLine.setValue(Poi.Size)
        self.number = Nu
        self.annotation = Poi.Annotation
        self.modifyPointWindow.AnnotationTextLine.setText(Poi.AnnotationText)
        self.modifyPointWindow.AnnotationXLine.setValue(Poi.AnnotationX)
        self.modifyPointWindow.AnnotationYLine.setValue(Poi.AnnotationY)

        if self.annotation:

            self.modifyPointWindow.AnnonationMetod.setCurrentIndex(1)

        else:

            self.modifyPointWindow.AnnonationMetod.setCurrentIndex(0)

    def setAnnotationMetod(self):

        if self.modifyPointWindow.AnnonationMetod.currentText() == "No Annotation":

            self.modifyPointWindow.AnnotationTextLine.setEnabled(False)
            self.modifyPointWindow.AnnotationXLine.setEnabled(False)
            self.modifyPointWindow.AnnotationYLine.setEnabled(False)
            self.annotation = False

        else:

            self.modifyPointWindow.AnnotationTextLine.setEnabled(True)
            self.modifyPointWindow.AnnotationXLine.setEnabled(True)
            self.modifyPointWindow.AnnotationYLine.setEnabled(True)
            self.annotation = True

    def openColorDialog(self):

        # open a dialog to choose the color of the point

        color = QColorDialog.getColor()
        self.modifyPointWindow.PointColorLine.setText(color.name())

    def modifyPoint(self):

        if self.parent.theNameAlreadyExistJump(self.modifyPointWindow.PointNameLine.text(), self.parent.graphic.points, self.number):

            QMessageBox.warning(self, "WARNING", "The name of your point already exist")

        else:

            self.parent.graphic.points[self.number].Name           = self.modifyPointWindow.PointNameLine.text()
            self.parent.graphic.points[self.number].Color          = self.modifyPointWindow.PointColorLine.text()
            self.parent.graphic.points[self.number].PointX         = self.modifyPointWindow.PointXLine.value()
            self.parent.graphic.points[self.number].PointY         = self.modifyPointWindow.PointYLine.value()
            self.parent.graphic.points[self.number].Size           = self.modifyPointWindow.PointSizeLine.value()
            self.parent.graphic.points[self.number].Annotation     = self.annotation
            self.parent.graphic.points[self.number].AnnotationText = self.modifyPointWindow.AnnotationTextLine.text()
            self.parent.graphic.points[self.number].AnnotationX    = self.modifyPointWindow.AnnotationXLine.value()
            self.parent.graphic.points[self.number].AnnotationY    = self.modifyPointWindow.AnnotationYLine.value()
            self.parent.graphic.update()
            self.parent.ui.statusbar.showMessage(f"Point \"{self.modifyPointWindow.PointNameLine.text()}\" midified!")