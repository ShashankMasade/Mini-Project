import sys
import os
from equitiesentry import *
from PyQt5 import QtWidgets, QtGui, QtCore

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'eqre1'); 

import sqlite3
con = sqlite3.connect('sqlite/eqre1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertrain)
     self.ui.pushButton_2.clicked.connect(self.insertest)
     self.ui.pushButton_3.clicked.connect(self.flslocn)
     self.ui.pushButton_4.clicked.connect(self.cdataent)
    

  def insertest(self):
    with con:
      cur = con.cursor()
      riskcat = str(self.ui.lineEdit.text())
      prevclose = str(self.ui.lineEdit_3.text())
      daylow = str(self.ui.lineEdit_4.text())
      dayhigh = str(self.ui.lineEdit_5.text())
      prevvar = str(self.ui.lineEdit_6.text())	
      cur.execute('INSERT INTO testdata VALUES(?,?,?,?,?)',(prevclose,daylow,dayhigh,prevvar,riskcat))
      con.commit()

  def flslocn(self):
    os.system("python exectensor1.py")     
    
 
  def insertrain(self):
    with con:
      cur = con.cursor()
      riskcat = str(self.ui.lineEdit.text())
      prevclose = str(self.ui.lineEdit_3.text())
      daylow = str(self.ui.lineEdit_4.text())
      dayhigh = str(self.ui.lineEdit_5.text())
      prevvar = str(self.ui.lineEdit_6.text())	
      cur.execute('INSERT INTO traindata VALUES(?,?,?,?,?)',(prevclose,daylow,dayhigh,prevvar,riskcat))
      con.commit()

  def cdataent(self):
    os.system("python cdataentry1.py")
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
