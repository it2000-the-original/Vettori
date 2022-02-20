import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.axisartist.axislines import SubplotZero
from math import sin, cos, radians

# This class define a vector

class vector:

    def __init__(self, Nm, Sx, Sy, Ex, Ey, Color, An, At, Ax, Ay):

        self.Name = Nm
        self.StartX = Sx
        self.StartY = Sy
        self.EndX = Ex
        self.EndY = Ey
        self.Color = Color
        self.Annotation = An
        self.AnnotationText = At
        self.AnnotationX = Ax
        self.AnnotationY = Ay
        
# This class define a point

class point:
    
    def __init__(self, Nm, Px, Py, Si, Color, An, At, Ax, Ay):
        
        self.Name = Nm
        self.PointX = Px
        self.PointY = Py
        self.Size = Si
        self.Color = Color
        self.Annotation = An
        self.AnnotationText = At
        self.AnnotationX = Ax
        self.AnnotationY = Ay
        
# this class takes care of managing every element of the canvas

class Graphics:

    def __init__(self, parent):
        
        # creating the canvas

        self.manager = parent
        self.figura = plt.figure()
        self.ax = SubplotZero(self.figura, 111)
        self.figura.add_subplot(self.ax)
        self.canvas = FigureCanvas(self.figura)

        # these are the variable that contain the names of
        # the x and y axis, and the canvas

        self.stringname  = None   # Name of the canvas (None Default)
        self.xstringname = None   # Name of the x axis (None Default)
        self.ystringname = None   # Name of the y axis (None Default)
        self.size  = 16           # Size of the text of the name of the canvas
        self.xsize = 10           # Size of the text of the name of the x axis
        self.ysize = 10           # Size of the text of the name of the y axis

        # these are the bool variables that set if
        # show grid, legend, projections

        self.showgrid        = False
        self.showlegend      = False
        self.showprojections = False

        # these are the lists of the vectors, the
        # points in the canvas and the elements in the legend

        self.vettors = []

        self.points = []
        self.legend = []

        self.parent = parent
        self.update()

        self.figura

    def update(self):

        # these fuction redraws the element from 0.
        # I run this fuction for every modify at the canvas

        self.ax.clear()
        self.manager.ui.listVectors.clear()
        self.manager.ui.listPoints.clear()
        plt.axhline(y = 0, color="grey", zorder=2, linewidth=2)
        plt.axvline(x = 0, color="grey", zorder=2, linewidth=2)

        counter = 1

        # create a quiver for every element in the vettors list

        for l in self.vettors:

            self.ax.quiver(
                
                [l.StartX], [l.StartY], 
                [l.EndX - l.StartX], 
                [l.EndY - l.StartY], 
                scale=1, units = "inches", 
                angles='xy', scale_units='xy', 
                color = [l.Color], zorder=5, width=0.04
            )

            self.manager.addItemVector(f"{counter} {l.Name}")

            if l.EndY >= l.StartY: 
                pa = 10
                pay = -13

            else: 
                pa = -13
                pay = 10
            
            if self.showlegend:

                self.legend.append(mpatches.Patch(color=l.Color, label=f"v: {l.Name}"))

            if self.showprojections:

                if l.StartX != 0 and l.StartY != 0:

                    plt.plot([l.StartX, l.StartX], [l.StartY, 0], linestyle = "--", linewidth=1, color = "#004240")
                    plt.plot([l.StartX, 0], [l.StartY, l.StartY], linestyle = "--", linewidth=1, color = "#004240")

                    self.ax.annotate(
                        f"({round(l.EndX, 2)}, {round(l.EndY, 2)})",
                        zorder=7,
                        xy=(l.StartX, l.StartY),
                        textcoords="offset points",
                        xytext=(0,pay), ha='center',
                        bbox = dict(facecolor='#ffffff', edgecolor='#ffffff'))

                if l.EndX != 0 and l.EndY != 0:

                    plt.plot([l.EndX, l.EndX], [l.EndY, 0], linestyle = "--", linewidth=1, color = "#004240")
                    plt.plot([l.EndX, 0], [l.EndY, l.EndY], linestyle = "--", linewidth=1, color = "#004240")

                    self.ax.annotate(
                        f"({round(l.EndX, 2)}, {round(l.EndY, 2)})",
                        zorder=7,
                        xy=(l.EndX, l.EndY),
                        textcoords="offset points",
                        xytext=(0,pa), ha='center',
                        bbox = dict(facecolor='#ffffff', edgecolor='#ffffff'))

            if l.Annotation:

                self.ax.annotate(
                    l.AnnotationText,
                    zorder=8,
                    xy=(l.StartX + (l.EndX - l.StartX) / 2, l.StartY + (l.EndY - l.StartY) / 2), 
                    xytext=(l.AnnotationX, l.AnnotationY), arrowprops=dict(arrowstyle = "-"), 
                    bbox = dict(facecolor='#ffffff', edgecolor='black', 
                    boxstyle='round,pad=0.5'))

            counter += 1
            
        counter = 1
            
        # create a quiver for every element in the points list

        for l in self.points:

            self.ax.scatter(x=l.PointX, y=l.PointY, s=l.Size, c=l.Color, zorder=6)
            self.manager.addItemPoint(f"{counter} {l.Name}")

            if self.showlegend == True:

                self.legend.append(mpatches.Patch(color=l.Color, label=f"p: {l.Name}"))

            if l.Annotation:

                self.ax.annotate(
                    l.AnnotationText,
                    zorder=7,
                    xy=(l.PointX, l.PointY), 
                    xytext=(l.AnnotationX, l.AnnotationY), arrowprops=dict(arrowstyle = "-"), 
                    bbox = dict(facecolor='#ffffff', edgecolor='black', 
                    boxstyle='round,pad=0.5'))

            counter += 1

        # setup the canvas

        if self.showgrid: plt.grid(True)
        else: plt.grid(False)
        if self.showlegend == True: self.ax.legend(handles=self.legend)
        self.ax.set_ylabel(self.ystringname, fontsize=self.ysize)
        self.ax.set_xlabel(self.xstringname, fontsize=self.xsize)
        self.setCamera()
        self.canvas.draw()
        self.legend.clear()

    # export an image in a specific directory

    def exportImage(self, dir):

        self.figura.savefig(dir)

    # add a vector in the list and update the canvas

    def addVector(self, Nm, Sx, Sy, Ex, Ey, Color, An, At, Ax, Ay):

        self.vettors.append(vector(Nm, Sx, Sy, Ex, Ey, Color, An, At, Ax, Ay))
        self.update()

    # add a point in the list and update the canvas
        
    def addPoint(self, Nm, Px, Py, Si, Color, An, At, Ax, Ay):
        
        self.points.append(point(Nm, Px, Py, Si, Color, An, At, Ax, Ay))
        self.update()

    # calculate the points of a vector with the size and the inclination
        
    def addVectorWithInclination(self, Nm, Sx, Sy, Si, In, InType, Color, An, At, Ax, Ay):
        
        if InType == "x":
            
            XSize = round(Si * cos(radians(In)), 2)
            YSize = round(Si * sin(radians(In)), 2)
            
        elif InType == "y":
            
            XSize = Si * sin(radians(In))
            YSize = Si * cos(radians(In))

        self.vettors.append(vector(Nm, Sx, Sy, Sx + XSize, Sy + YSize, Color, An, At, Ax, Ay))
        self.update()

    # remove a vector from from the list and update the canvas

    def removeVector(self, num):

        self.vettors.pop(num)
        self.update()
        
    # remove a point from from the list and update the canvas

    def removePoint(self, num):

        self.points.pop(num)
        self.update()

    # calculate a vector sum of two vectors
        
    def generateSumVector(self, Nm, Sx, Sy, V1, V2, Color, An, At, Ax, Ay):
        
        P1x = self.vettors[V1].EndX + (Sx - self.vettors[V1].StartX)
        P1y = self.vettors[V1].EndY + (Sy - self.vettors[V1].StartY)
        P2x = self.vettors[V2].EndX + (P1x - self.vettors[V2].StartX)
        P2y = self.vettors[V2].EndY + (P1y - self.vettors[V2].StartY)
        
        self.vettors.append(vector(Nm, Sx, Sy, P2x, P2y, Color, An, At, Ax, Ay))
        self.update()

    # calculate a vector subtract of two vectors

    def generateSubtractVector(self, Nm, Sx, Sy, V1, V2, Color, An, At, Ax, Ay):

        P1x = self.vettors[V1].EndX + (Sx - self.vettors[V1].StartX)
        P1y = self.vettors[V1].EndY + (Sy - self.vettors[V1].StartY)
        P2x = self.vettors[V2].StartX + (P1x - self.vettors[V2].EndX)
        P2y = self.vettors[V2].StartY + (P1y - self.vettors[V2].EndY)

        self.vettors.append(vector(Nm, Sx, Sy, P2x, P2y, Color, An, At, Ax, Ay))
        self.update()

    # fuctions to set the canvas names...

    def setName(self, name, size):

        self.stringname = name
        self.size = size
        plt.suptitle(self.stringname, fontsize=self.size)
        self.update()

    def setXname(self, name, size):

        self.xstringname = name
        self.xsize = size
        self.update()

    def setYname(self, name, size):

        self.ystringname = name
        self.ysize = size
        self.update()
        
    def setGrid(self, var):
        self.showgrid = var

    def getGrid(self):
        return self.showgrid

    # this function sets the xlim and ylim of the canvas to the 
    # lowest value found and the highest value along with some spacing

    def setCamera(self):

        MinX = 0
        MinY = 0
        MaxX = 0
        MaxY = 0

        for l in self.vettors:

            if l.StartX < MinX: MinX = l.StartX
            elif l.StartX > MaxX: MaxX = l.StartX
            if l.StartY < MinY: MinY = l.StartY
            elif l.StartY > MaxY: MaxY = l.StartY
            if l.EndX < MinX: MinX = l.EndX
            elif l.EndX > MaxX: MaxX = l.EndX
            if l.EndY < MinY: MinY = l.EndY
            elif l.EndY > MaxY: MaxY = l.EndY

        for l in self.points:

            if l.PointX < MinX: MinX = l.PointX
            elif l.PointX > MaxX: MaxX = l.PointX
            if l.PointY < MinY: MinY = l.PointY
            elif l.PointY > MaxY: MaxY = l.PointY

        if MinX == 0 and MinY == 0 and len(self.vettors) == 0:
            
            MaxX *= 2
            MaxY *= 2
            
        elif MaxX == 0 and MaxY == 0 and len(self.vettors) == 0:
            
            MinX *= 2
            MinY *= 2
            
        XSize = abs(MinX - MaxX)
        YSize = abs(MinY - MaxY)
        MinX -= XSize / 20
        XSize += XSize / 10
        MinY -= YSize / 20
        YSize += YSize / 10

        if MinX == MinY == XSize == YSize == 0:

            self.ax.set_xlim(-1, 1)
            self.ax.set_ylim(-1, 1)

        else:

            self.ax.set_xlim(MinX, MinX + XSize)
            self.ax.set_ylim(MinY, MinY + YSize)