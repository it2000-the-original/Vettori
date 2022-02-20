from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import *
from window import *
import os

# Dialogs
from AddVectorManager import *
from AddPointManager import *
from RemoveVectorManager import *
from RemovePointManager import *
from GenerateSumVecotrManager import *
from GenerateSubtractVectorManager import *
from ModifyVectorManager import *
from ModifyPointManager import *
from NameManager import *
from XNameManager import *
from YNameManager import *

from graphics import *
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import pickle

###################################### About menu messages ##################################################
                                                                                                            
infotext = """Vectors is a physical representation of vector forces has two tables of                       
elements inserted in the board, one for vectors and one for points.                                       
Written in python with the following libraries:

pyqt5: Graphical Interfaces
matplotlib: Graphical representation
pickle: Save to file"""

helptext = """to create a new file press Ctrl + N or go to File-> New File 
while if you want to open a file, press Ctrl + O or go to 
File-> Open File. If you want to save your representation go 
to File-> Save File and File-> Save New, the shortcut is 
indicated on the button. Similarly, the Edit section takes 
care of editing its representation while the Settings section 
takes care of setting the various display modes."""

versiontext = "Vettori version 0.2"

#############################################################################################################

class Manager(QtWidgets.QMainWindow):

    def __init__(self, file):

        # init the class and setup the window

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(f"{os.path.dirname(__file__)}/icons/vettori.svg"))
        
        # variables to see the previous directory where a file has been saved or opened

        self.exfile = None
        self.exfile2 = None
        self.exdirectory = None
        self.filename = None

        # initialize the lass "Graphics and add the canvas to the MatplotArea widget"

        self.graphic = Graphics(self)
        self.ui.MatplotArea.addWidget(self.graphic.canvas)

        # Classes for every dialog window in the mainwindow

        self.addvectormanager              = AddVectorManager(self)
        self.addpointmanager               = AddPointManager(self)
        self.removevectormanager           = RemoveVectorManager(self)
        self.removepointmanager            = RemovePointManager(self)
        self.generatesumvectormanager      = GenerateSumVectorManager(self)
        self.generatesubtractvectormanager = GenerateSubtractVectorManager(self)
        self.modifyvectormanager           = ModifyVectorManager(self)
        self.modifypointmanager            = ModifyPointManager(self)
        self.namemanager                   = NameManager(self)
        self.xnamemanager                  = XNameManager(self)
        self.ynamemanager                  = YNameManager(self)

        # adding the right commands for every action of the menubar

        self.ui.actionAdd_Vector.triggered.connect(self.addVector)
        self.ui.actionAdd_Point.triggered.connect(self.addPoint)
        self.ui.actionRemove_Vector.triggered.connect(self.removeVector)
        self.ui.actionRemove_Point.triggered.connect(self.removePoint)
        self.ui.actionGenerate_Sum_Vector.triggered.connect(self.generateSumVector)
        self.ui.actionGenerate_Subtract_Vector.triggered.connect(self.generateSubtractVector)
        self.ui.actionAdd_Legend.triggered.connect(self.EnableDisableLegend)
        self.ui.actionShow_Projections.triggered.connect(self.EnableDisableProjections)
        self.ui.actionShow_Hide_Grid.triggered.connect(self.EnableDisableGrid)
        self.ui.actionSet_Name.triggered.connect(self.setName)
        self.ui.actionSet_XLabel_Name.triggered.connect(self.setXName)
        self.ui.actionSet_YLabel_Name.triggered.connect(self.setYName)
        self.ui.actionExport_Image.triggered.connect(self.SaveCurrentImage)
        self.ui.actionNew_File.triggered.connect(self.NewFile)
        self.ui.actionSave_File.triggered.connect(self.SaveFile)
        self.ui.actionOpen_File.triggered.connect(self.OpenFile)
        self.ui.actionSave_New.triggered.connect(self.SaveNewFile)
        self.ui.actionInfo.triggered.connect(self.InfoShow)
        self.ui.actionHelp.triggered.connect(self.HelpShow)
        self.ui.actionVersion.triggered.connect(self.VersionShow)

        # connecting other commands...

        self.ui.listVectors.itemDoubleClicked.connect(self.modifyVector)
        self.ui.listPoints.itemDoubleClicked.connect(self.modifyPoint)
        self.ui.LegendBox.clicked.connect(self.EnableDisableLegend)
        self.ui.ProjectionsBox.clicked.connect(self.EnableDisableProjections)
        self.ui.GridBox.clicked.connect(self.EnableDisableGrid)
        self.ui.statusbar.messageChanged.connect(self.FoundChange)

        # adding the toolbar to the QMainWindow (default toolbar of matplotlib)

        self.toolbar = NavigationToolbar(self.graphic.canvas, self)
        self.addToolBar(self.toolbar)

        # show the window, enable the grid, set the title and the statusbar message

        self.show()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.EnableDisableGrid()
        self.setWindowTitle("Vettori 0.2 - Physical vectors rappresentation")
        self.ui.statusbar.showMessage("Vettori 0.2 - Physical vectors rappresentation")

        # if file parameter is passed execute the OpenFilePaeameter fuction

        if file:
            self.OpenFilePaeameter(file)

    def InfoShow(self):
        QMessageBox.information(self, "Vettori info", infotext)

    def HelpShow(self):
        QMessageBox.information(self, "Vettori Help", helptext)

    def VersionShow(self):
        QMessageBox.information(self, "Vettori Version", versiontext)

    def FoundChange(self):

        if self.ui.statusbar.currentMessage() == "":
            self.ui.statusbar.showMessage("Vettori 0.2 - Physical vectors rappresentation")

    def NewFile(self):

        # this reset all variable of the status

        if len(self.graphic.vettors) == len(self.graphic.points) == 0:
            ret = 16384
        else:
            ret = QMessageBox.question(self, 'New File', "Are you sure? All unsaved changes will be lost!")

        if ret != 65536:
            self.filename = None
            self.graphic.vettors = []
            self.graphic.points = []
            self.graphic.setName("",0)
            self.graphic.setXname("",0)
            self.graphic.setYname("",0)
            self.graphic.update()
            self.ui.statusbar.showMessage("New file has been created! (filename = None)")
            self.setWindowTitle("Vettori 0.2 - Untitled.vet")

    def SaveFile(self):

        # if filename variable is different from "None" save the file in that directory else execute SaveNewFile

        if self.filename:

            data = [ 
                self.graphic.xstringname,
                self.graphic.xsize,
                self.graphic.ystringname,
                self.graphic.ysize,
                self.graphic.stringname,
                self.graphic.size,
                [], []
            ]

            for l in self.graphic.vettors:

                list = []
                list.append(l.Name) 
                list.append(l.StartX)
                list.append(l.StartY) 
                list.append(l.EndX)
                list.append(l.EndY)
                list.append(l.Color)
                list.append(l.Annotation)
                list.append(l.AnnotationText)
                list.append(l.AnnotationX)
                list.append(l.AnnotationY)
                data[6].append(list)

            for l in self.graphic.points:

                list = []
                list.append(l.Name)
                list.append(l.PointX)
                list.append(l.PointY)
                list.append(l.Size)
                list.append(l.Color)
                list.append(l.Annotation)
                list.append(l.AnnotationText)
                list.append(l.AnnotationX)
                list.append(l.AnnotationY)

                data[7].append(list)

            with open(self.filename, "wb") as f:
                pickle.dump(data, f)

            self.ui.statusbar.showMessage(f"Your file has been overwritten in {self.filename} directory!")
            self.setWindowTitle(f"Vettori 0.2 - {self.filename}")

        else:

            self.SaveNewFile()

    def SaveNewFile(self):

        # to save file I open a QFileDialog to path to the directory doosed
        # by the user and create a list witch contain the data of the actual situation
        # and with the pickle library, dump this list in a binary file in .vet format

        if self.exfile2:
            filename = QFileDialog.getSaveFileName(self, caption='Save New File', filter="Vettori file (*.vet)", directory=self.exfile2)

        else:
            filename = QFileDialog.getSaveFileName(self, caption='Save New File', filter="Vettori file (*.vet)", directory="Untitled.vet")
        
        if filename[0] != '':

            self.filename = filename[0]
            self.exfile2 = filename[0]

            data = [ 
                self.graphic.xstringname,
                self.graphic.xsize,
                self.graphic.ystringname,
                self.graphic.ysize,
                self.graphic.stringname,
                self.graphic.size,
                [], []
            ]

            for l in self.graphic.vettors:

                list = []
                list.append(l.Name) 
                list.append(l.StartX) 
                list.append(l.StartY) 
                list.append(l.EndX)
                list.append(l.EndY)
                list.append(l.Color)
                list.append(l.Annotation)
                list.append(l.AnnotationText)
                list.append(l.AnnotationX)
                list.append(l.AnnotationY)
                data[6].append(list)

            for l in self.graphic.points:

                list = []
                list.append(l.Name)
                list.append(l.PointX)
                list.append(l.PointY)
                list.append(l.Size)
                list.append(l.Color)
                list.append(l.Annotation)
                list.append(l.AnnotationText)
                list.append(l.AnnotationX)
                list.append(l.AnnotationY)
                data[7].append(list)

            with open(self.filename, "wb") as f:    
                pickle.dump(data, f)

            self.ui.statusbar.showMessage(f"Your file has been saved in \"{self.filename}\" directory!")
            self.setWindowTitle(f"Vettori 0.2 - {self.filename}")

    def OpenFilePaeameter(self, file):

        # if was passed a parameter, open that as file

        with open(file, "rb") as f:
            data = pickle.load(f)

        self.graphic.setXname(data[0], data[1])
        self.graphic.setYname(data[2], data[3])
        self.graphic.setName(data[4], data[5])
        self.graphic.vettors = []
        self.graphic.points = []

        for l in data[6]:
            self.graphic.addVector(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9])

        for l in data[7]:
            self.graphic.addPoint(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8])
        
        self.graphic.update()
        self.filename = file

        self.ui.statusbar.showMessage(f"File opened from \"{self.filename}\" directory!")
        self.setWindowTitle(f"Vettori 0.2 - {self.filename}")

    def OpenFile(self):

        # To open a file with pickle load a data vector from the file
        # and I set every variable of the situation

        if len(self.graphic.vettors) == len(self.graphic.points) == 0:
            ret = 16384
            
        else:
            ret = QMessageBox.question(self, 'Open File', "Are you sure? All unsaved changes will be lost!")

        if ret != 65536:
            if self.exdirectory:
                filename = QFileDialog.getOpenFileName(self, caption='Open File', filter="Vettori file (*.vet)", directory=self.exdirectory)

            else:
                filename = QFileDialog.getOpenFileName(self, caption='Save New File', filter="Vettori file (*.vet)")

            if filename[0] != '':
                
                self.filename = filename[0]
                self.exdirectory = filename[0]
                with open(self.filename, "rb") as f:
                    data = pickle.load(f)

                self.graphic.setXname(data[0], data[1])
                self.graphic.setYname(data[2], data[3])
                self.graphic.setName(data[4], data[5])
                self.graphic.vettors = []
                self.graphic.points = []

                for l in data[6]:
                    self.graphic.addVector(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9])

                for l in data[7]:
                    self.graphic.addPoint(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8])
                
                self.graphic.update()

                self.ui.statusbar.showMessage(f"File opened from \"{self.filename}\" directory!")
                self.setWindowTitle(f"Vettori 0.2 - {self.filename}")

    def SaveCurrentImage(self):

        # this export the canvas image as a file in .png format

        if self.exfile:
            filename = QFileDialog.getSaveFileName(self, caption='Export Current Image', filter="Image file (*.png)", directory=self.exfile)

        else:
            filename = QFileDialog.getSaveFileName(self, caption='Export Current Image', filter="Image file (*.png)", directory="Untitled.png")
        
        if filename[0] != '':
            self.exfile = filename[0]
            self.graphic.exportImage(filename[0])
            self.ui.statusbar.showMessage(f"Image exported in \"{self.exfile}\" directory!")

    def EnableDisableGrid(self):

        # Turn on/off the grid

        if self.graphic.getGrid() == True: 
            self.graphic.setGrid(False)
            self.ui.statusbar.showMessage("Grid disabled!")

        else: 
            self.graphic.setGrid(True)
            self.ui.statusbar.showMessage("Grid enabled!")

        if self.graphic.showgrid == True: self.ui.GridBox.setChecked(True)
        else: self.ui.GridBox.setChecked(False)
        self.graphic.update()
    
    def EnableDisableLegend(self):

        # Turn on/off the the legend

        if self.graphic.showlegend == True:
            self.graphic.showlegend = False
            self.ui.statusbar.showMessage("Legend disabled!")

        else: 
            self.graphic.showlegend = True
            self.ui.statusbar.showMessage("Legend enabled!")

        if self.graphic.showlegend == True: self.ui.LegendBox.setChecked(True)
        else: self.ui.LegendBox.setChecked(False)
        self.graphic.update()

    def EnableDisableProjections(self):

        # Turn on/off the projections

        if self.graphic.showprojections == True: 
            self.graphic.showprojections = False
            self.ui.statusbar.showMessage("Projections disabled!")

        else: 
            self.graphic.showprojections = True
            self.ui.statusbar.showMessage("Projections enabled!")
            
        if self.graphic.showprojections == True: self.ui.ProjectionsBox.setChecked(True)
        else: self.ui.ProjectionsBox.setChecked(False)
        self.graphic.update()

    def addVector(self):

        self.addvectormanager.clear()
        self.addvectormanager.exec()
        
    def addPoint(self):

        self.addpointmanager.clear()
        self.addpointmanager.exec()

    def removeVector(self):

        self.removevectormanager.clear()
        self.removevectormanager.exec()

    def removePoint(self):

        self.removepointmanager.clear()
        self.removepointmanager.exec()
     
    def generateSumVector(self):
        
        self.generatesumvectormanager.clear()
        self.generatesumvectormanager.exec()

    def generateSubtractVector(self):
        
        self.generatesubtractvectormanager.clear()
        self.generatesubtractvectormanager.exec()

    def modifyVector(self):

        self.modifyvectormanager.setVector(self.graphic.vettors[self.ui.listVectors.currentRow()], self.ui.listVectors.currentRow())
        self.modifyvectormanager.exec()

    def modifyPoint(self):

        self.modifypointmanager.setPoint(self.graphic.points[self.ui.listPoints.currentRow()], self.ui.listPoints.currentRow())
        self.modifypointmanager.exec()

    def setName(self):

        self.namemanager.clear()
        self.namemanager.exec()

    def setXName(self):

        self.xnamemanager.clear()
        self.xnamemanager.exec()

    def setYName(self):

        self.ynamemanager.clear()
        self.ynamemanager.exec()

    # This fuctions add an item in the listbox of the element
    # that has been added
        
    def addItemVector(self, text):
    
        self.ui.listVectors.addItem(text)
        
    def addItemPoint(self, text):
    
        self.ui.listPoints.addItem(text)

    # This check if a name already exist in a element of the canvas
        
    def theNameAlreadyExist(self, name, vet):
        
        var = False
        
        for n in vet:
            if n.Name == name:
                var = True
                
        return var

    # The fuction but jump a element

    def theNameAlreadyExistJump(self, name, vet, jump):
        
        var = False
        cont = 0

        for n in vet:
            if cont != jump:
                if n.Name == name:
                    var = True

            cont += 1
        return var

if __name__ == "__main__":
    import sys
    par = sys.argv

    if len(par) > 2:
        print("Error: you can open a max of one file!")

    else:

        if len(par) == 2:

            try:
            
                with open(par[1], "rb") as f: pass
                app = QtWidgets.QApplication(par)
                # This lines commented will be enable in
                # future version of Vettori
                #file = QFile("")
                #file.open(QFile.ReadOnly | QFile.Text)
                #stream = QTextStream(file)
                #app.setStyleSheet(stream.readAll())
                manager = Manager(par[1])
                sys.exit(app.exec_())
            
            except Exception as e:
                print(f"Error to open the file: {e}")

        else:
            
            app = QtWidgets.QApplication(par)
            # This lines commented will be enable in
            # future version of Vettori
            #file = QFile("")
            #file.open(QFile.ReadOnly | QFile.Text)
            #stream = QTextStream(file)
            #app.setStyleSheet(stream.readAll())
            manager = Manager(None)
            sys.exit(app.exec_())