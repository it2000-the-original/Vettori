# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifypointDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModifyPoint(object):
    def setupUi(self, ModifyPoint):
        ModifyPoint.setObjectName("ModifyPoint")
        ModifyPoint.resize(485, 268)
        ModifyPoint.setMinimumSize(QtCore.QSize(485, 268))
        self.gridLayout = QtWidgets.QGridLayout(ModifyPoint)
        self.gridLayout.setObjectName("gridLayout")
        self.OkButton = QtWidgets.QPushButton(ModifyPoint)
        self.OkButton.setDefault(True)
        self.OkButton.setObjectName("OkButton")
        self.gridLayout.addWidget(self.OkButton, 7, 3, 1, 1)
        self.ApplyButton = QtWidgets.QPushButton(ModifyPoint)
        self.ApplyButton.setAutoDefault(False)
        self.ApplyButton.setObjectName("ApplyButton")
        self.gridLayout.addWidget(self.ApplyButton, 7, 1, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(ModifyPoint)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PointNameLine = QtWidgets.QLineEdit(self.tab)
        self.PointNameLine.setObjectName("PointNameLine")
        self.gridLayout_2.addWidget(self.PointNameLine, 0, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.AnnotationYLine = QtWidgets.QDoubleSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnnotationYLine.sizePolicy().hasHeightForWidth())
        self.AnnotationYLine.setSizePolicy(sizePolicy)
        self.AnnotationYLine.setMinimum(-999999999.99)
        self.AnnotationYLine.setMaximum(999999999.99)
        self.AnnotationYLine.setObjectName("AnnotationYLine")
        self.gridLayout_2.addWidget(self.AnnotationYLine, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.AnnotationTextLine = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnnotationTextLine.sizePolicy().hasHeightForWidth())
        self.AnnotationTextLine.setSizePolicy(sizePolicy)
        self.AnnotationTextLine.setObjectName("AnnotationTextLine")
        self.gridLayout_2.addWidget(self.AnnotationTextLine, 2, 1, 1, 1)
        self.PointColorLine = QtWidgets.QLineEdit(self.tab)
        self.PointColorLine.setObjectName("PointColorLine")
        self.gridLayout_2.addWidget(self.PointColorLine, 1, 1, 1, 1)
        self.AnnonationMetod = QtWidgets.QComboBox(self.tab)
        self.AnnonationMetod.setObjectName("AnnonationMetod")
        self.AnnonationMetod.addItem("")
        self.AnnonationMetod.addItem("")
        self.gridLayout_2.addWidget(self.AnnonationMetod, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.AnnotationXLine = QtWidgets.QDoubleSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnnotationXLine.sizePolicy().hasHeightForWidth())
        self.AnnotationXLine.setSizePolicy(sizePolicy)
        self.AnnotationXLine.setMinimum(-999999999.99)
        self.AnnotationXLine.setMaximum(999999999.99)
        self.AnnotationXLine.setObjectName("AnnotationXLine")
        self.gridLayout_2.addWidget(self.AnnotationXLine, 3, 1, 1, 2)
        self.PathColorButton = QtWidgets.QPushButton(self.tab)
        self.PathColorButton.setAutoDefault(False)
        self.PathColorButton.setObjectName("PathColorButton")
        self.gridLayout_2.addWidget(self.PathColorButton, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 443, 170))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PointYLine = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointYLine.sizePolicy().hasHeightForWidth())
        self.PointYLine.setSizePolicy(sizePolicy)
        self.PointYLine.setMinimum(-999999999.99)
        self.PointYLine.setMaximum(999999999.99)
        self.PointYLine.setSingleStep(0.1)
        self.PointYLine.setObjectName("PointYLine")
        self.gridLayout_4.addWidget(self.PointYLine, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.PointSizeLine = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointSizeLine.sizePolicy().hasHeightForWidth())
        self.PointSizeLine.setSizePolicy(sizePolicy)
        self.PointSizeLine.setMinimum(1.0)
        self.PointSizeLine.setMaximum(999999999.99)
        self.PointSizeLine.setSingleStep(1.0)
        self.PointSizeLine.setProperty("value", 50.0)
        self.PointSizeLine.setObjectName("PointSizeLine")
        self.gridLayout_4.addWidget(self.PointSizeLine, 2, 1, 1, 1)
        self.PointXLine = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointXLine.sizePolicy().hasHeightForWidth())
        self.PointXLine.setSizePolicy(sizePolicy)
        self.PointXLine.setMinimum(-999999999.99)
        self.PointXLine.setMaximum(999999999.99)
        self.PointXLine.setSingleStep(0.1)
        self.PointXLine.setProperty("value", 0.0)
        self.PointXLine.setObjectName("PointXLine")
        self.gridLayout_4.addWidget(self.PointXLine, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 3, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 3)

        self.retranslateUi(ModifyPoint)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ModifyPoint)

    def retranslateUi(self, ModifyPoint):
        _translate = QtCore.QCoreApplication.translate
        ModifyPoint.setWindowTitle(_translate("ModifyPoint", "Modify Point"))
        self.OkButton.setText(_translate("ModifyPoint", "Ok"))
        self.ApplyButton.setText(_translate("ModifyPoint", "Apply"))
        self.PointNameLine.setText(_translate("ModifyPoint", "Untitled"))
        self.label_11.setText(_translate("ModifyPoint", "Annotation x pos"))
        self.label.setText(_translate("ModifyPoint", "Point Name"))
        self.label_2.setText(_translate("ModifyPoint", "Point Color"))
        self.AnnotationTextLine.setText(_translate("ModifyPoint", "Annotation Text"))
        self.PointColorLine.setText(_translate("ModifyPoint", "#000000"))
        self.AnnonationMetod.setItemText(0, _translate("ModifyPoint", "No Annotation"))
        self.AnnonationMetod.setItemText(1, _translate("ModifyPoint", "Annotation"))
        self.label_12.setText(_translate("ModifyPoint", "Annotation y pos"))
        self.label_10.setText(_translate("ModifyPoint", "Annotation text"))
        self.PathColorButton.setText(_translate("ModifyPoint", "Path Color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ModifyPoint", "Visualization"))
        self.label_4.setText(_translate("ModifyPoint", "Point y position"))
        self.label_3.setText(_translate("ModifyPoint", "Point x position"))
        self.label_5.setText(_translate("ModifyPoint", "Point size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ModifyPoint", "Position and size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyPoint = QtWidgets.QDialog()
    ui = Ui_ModifyPoint()
    ui.setupUi(ModifyPoint)
    ModifyPoint.show()
    sys.exit(app.exec_())
