# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generatesubtractvectorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GenerateSubtractVector(object):
    def setupUi(self, GenerateSubtractVector):
        GenerateSubtractVector.setObjectName("GenerateSubtractVector")
        GenerateSubtractVector.resize(534, 273)
        GenerateSubtractVector.setMinimumSize(QtCore.QSize(534, 273))
        self.gridLayout = QtWidgets.QGridLayout(GenerateSubtractVector)
        self.gridLayout.setObjectName("gridLayout")
        self.GenerateSubtractVectorButton = QtWidgets.QPushButton(GenerateSubtractVector)
        self.GenerateSubtractVectorButton.setDefault(True)
        self.GenerateSubtractVectorButton.setObjectName("GenerateSubtractVectorButton")
        self.gridLayout.addWidget(self.GenerateSubtractVectorButton, 5, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(GenerateSubtractVector)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 486, 175))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)
        self.VectorColorLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VectorColorLine.sizePolicy().hasHeightForWidth())
        self.VectorColorLine.setSizePolicy(sizePolicy)
        self.VectorColorLine.setObjectName("VectorColorLine")
        self.gridLayout_3.addWidget(self.VectorColorLine, 1, 1, 1, 1)
        self.PathColorButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathColorButton.sizePolicy().hasHeightForWidth())
        self.PathColorButton.setSizePolicy(sizePolicy)
        self.PathColorButton.setAutoDefault(False)
        self.PathColorButton.setObjectName("PathColorButton")
        self.gridLayout_3.addWidget(self.PathColorButton, 1, 2, 1, 1)
        self.AnnotationYLine = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.AnnotationYLine.setMinimum(-999999999.99)
        self.AnnotationYLine.setMaximum(999999999.99)
        self.AnnotationYLine.setObjectName("AnnotationYLine")
        self.gridLayout_3.addWidget(self.AnnotationYLine, 5, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 0, 1, 1)
        self.VectorNameLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.VectorNameLine.setObjectName("VectorNameLine")
        self.gridLayout_3.addWidget(self.VectorNameLine, 0, 1, 1, 2)
        self.AnnotationXLine = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.AnnotationXLine.setMinimum(-999999999.99)
        self.AnnotationXLine.setMaximum(999999999.99)
        self.AnnotationXLine.setObjectName("AnnotationXLine")
        self.gridLayout_3.addWidget(self.AnnotationXLine, 4, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 6, 0, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.AnnotationTextLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.AnnotationTextLine.setObjectName("AnnotationTextLine")
        self.gridLayout_3.addWidget(self.AnnotationTextLine, 3, 1, 1, 1)
        self.AnnonationMetod = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnnonationMetod.sizePolicy().hasHeightForWidth())
        self.AnnonationMetod.setSizePolicy(sizePolicy)
        self.AnnonationMetod.setObjectName("AnnonationMetod")
        self.AnnonationMetod.addItem("")
        self.AnnonationMetod.addItem("")
        self.gridLayout_3.addWidget(self.AnnonationMetod, 3, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 555, 186))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.point_of_origin_y_Line = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_of_origin_y_Line.sizePolicy().hasHeightForWidth())
        self.point_of_origin_y_Line.setSizePolicy(sizePolicy)
        self.point_of_origin_y_Line.setMinimum(-999999999.0)
        self.point_of_origin_y_Line.setMaximum(999999999.0)
        self.point_of_origin_y_Line.setSingleStep(0.1)
        self.point_of_origin_y_Line.setObjectName("point_of_origin_y_Line")
        self.gridLayout_5.addWidget(self.point_of_origin_y_Line, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.ComboSecondVectors = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboSecondVectors.sizePolicy().hasHeightForWidth())
        self.ComboSecondVectors.setSizePolicy(sizePolicy)
        self.ComboSecondVectors.setObjectName("ComboSecondVectors")
        self.gridLayout_5.addWidget(self.ComboSecondVectors, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.point_of_origin_x_Line = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_of_origin_x_Line.sizePolicy().hasHeightForWidth())
        self.point_of_origin_x_Line.setSizePolicy(sizePolicy)
        self.point_of_origin_x_Line.setMinimum(-999999999.0)
        self.point_of_origin_x_Line.setMaximum(999999999.0)
        self.point_of_origin_x_Line.setSingleStep(0.1)
        self.point_of_origin_x_Line.setObjectName("point_of_origin_x_Line")
        self.gridLayout_5.addWidget(self.point_of_origin_x_Line, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.ComboFirstVectors = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboFirstVectors.sizePolicy().hasHeightForWidth())
        self.ComboFirstVectors.setSizePolicy(sizePolicy)
        self.ComboFirstVectors.setObjectName("ComboFirstVectors")
        self.gridLayout_5.addWidget(self.ComboFirstVectors, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 4, 0, 1, 2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 4, 0, 1, 1)

        self.retranslateUi(GenerateSubtractVector)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GenerateSubtractVector)

    def retranslateUi(self, GenerateSubtractVector):
        _translate = QtCore.QCoreApplication.translate
        GenerateSubtractVector.setWindowTitle(_translate("GenerateSubtractVector", "Generate Subtract Vector"))
        self.GenerateSubtractVectorButton.setText(_translate("GenerateSubtractVector", "Generate Subtract Vector"))
        self.label_15.setText(_translate("GenerateSubtractVector", "Vector Color"))
        self.VectorColorLine.setText(_translate("GenerateSubtractVector", "#000000"))
        self.PathColorButton.setText(_translate("GenerateSubtractVector", "Path Color"))
        self.label_19.setText(_translate("GenerateSubtractVector", "Annotation y pos"))
        self.VectorNameLine.setText(_translate("GenerateSubtractVector", "Untitled"))
        self.label_18.setText(_translate("GenerateSubtractVector", "Annotation x pos"))
        self.label_16.setText(_translate("GenerateSubtractVector", "Annotation Text"))
        self.label_17.setText(_translate("GenerateSubtractVector", "Vector Name"))
        self.AnnotationTextLine.setText(_translate("GenerateSubtractVector", "Annotation Text"))
        self.AnnonationMetod.setItemText(0, _translate("GenerateSubtractVector", "No Annotation"))
        self.AnnonationMetod.setItemText(1, _translate("GenerateSubtractVector", "Annotation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("GenerateSubtractVector", "Visualization"))
        self.label_2.setText(_translate("GenerateSubtractVector", "point of origin x"))
        self.label.setText(_translate("GenerateSubtractVector", "point of origin y"))
        self.label_3.setText(_translate("GenerateSubtractVector", "First Vector"))
        self.label_4.setText(_translate("GenerateSubtractVector", "Second Vector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("GenerateSubtractVector", "Position and size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerateSubtractVector = QtWidgets.QDialog()
    ui = Ui_GenerateSubtractVector()
    ui.setupUi(GenerateSubtractVector)
    GenerateSubtractVector.show()
    sys.exit(app.exec_())
