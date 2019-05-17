from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('sqlite/eqre1')

comment the existing DB connections.

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.pdetails)
     self.ui.pushButton_2.clicked.connect(self.imgone)
     self.ui.pushButton_3.clicked.connect(self.imgtwo)
     self.ui.pushButton_4.clicked.connect(self.psympts)
     self.ui.pushButton_5.clicked.connect(self.ptstrslts)


change the tab spaces in the define functions

replace %s with ?

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


