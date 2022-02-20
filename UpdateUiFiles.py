import os

os.chdir("Ui Files")

os.system("pyuic5 -x addvectorDialog.ui -o ../source/Dialogs/AddVectorDialog.py")
os.system("pyuic5 -x addpointDialog.ui -o ../source/Dialogs/AddPointDialog.py")
os.system("pyuic5 -x removevectorDialog.ui -o ../source/Dialogs/RemoveVectorDialog.py")
os.system("pyuic5 -x removepointDialog.ui -o ../source/Dialogs/RemovePointDialog.py")
os.system("pyuic5 -x generatesumvectorDialog.ui -o ../source/Dialogs/GenerateSumVectorDialog.py")
os.system("pyuic5 -x generatesubtractvectorDialog.ui -o ../source/Dialogs/GenerateSubtractVectorDialog.py")
os.system("pyuic5 -x modifyvectorDialog.ui -o ../source/Dialogs/ModifyVectorDialog.py")
os.system("pyuic5 -x vectors.ui -o ../source/window.py")
os.system("pyuic5 -x modifypointDialog.ui -o ../source/Dialogs/ModifyPointDialog.py")
os.system("pyuic5 -x nameDialog.ui -o ../source/Dialogs/NameDialog.py")
os.system("pyuic5 -x xnameDialog.ui -o ../source/Dialogs/XNameDialog.py")
os.system("pyuic5 -x ynameDialog.ui -o ../source/Dialogs/YNameDialog.py")
os.chdir("..")
