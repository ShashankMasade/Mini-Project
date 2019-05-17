#This program gets two values from a DB into lineEdits.
import sys
import os
from cdataentry import *
from PyQt5 import QtWidgets, QtGui, QtCore

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'eqre1'); 

import sqlite3
try:
    con = sqlite3.connect('sqlite/eqre1')
except lite.OperationalError:
    mkdir('sqlite')
finally:
    con = sqlite3.connect('sqlite/eqre1')
#con = sqlite3.connect('sqlite/eqre1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertest1)
     self.ui.pushButton_2.clicked.connect(self.insertest2)
     self.ui.pushButton_3.clicked.connect(self.insertest3)
     self.ui.pushButton_4.clicked.connect(self.csvcreate)
 

  def insertest1(self):
    with con:
      cur = con.cursor()
      riskcat = str(self.ui.lineEdit.text())
      pclose = str(self.ui.lineEdit_3.text())
      dlow = str(self.ui.lineEdit_4.text())
      dhigh = str(self.ui.lineEdit_5.text())
      pvar = str(self.ui.lineEdit_6.text())	
      cur.execute('INSERT INTO ctestdata VALUES(?,?,?,?,?)',(pclose,dlow,dhigh,pvar,riskcat))
      con.commit()

  def insertest2(self):
    with con:
      cur = con.cursor()
      riskcat = str(self.ui.lineEdit_2.text())
      pclose = str(self.ui.lineEdit_9.text())
      dlow = str(self.ui.lineEdit_8.text())
      dhigh = str(self.ui.lineEdit_7.text())
      pvar = str(self.ui.lineEdit_10.text())	
      cur.execute('INSERT INTO ctestdata VALUES(?,?,?,?,?)',(pclose,dlow,dhigh,pvar,riskcat))
      con.commit()

  def insertest3(self):
    with con:
      cur = con.cursor()
      riskcat = str(self.ui.lineEdit_13.text())
      pclose = str(self.ui.lineEdit_14.text())
      dlow = str(self.ui.lineEdit_12.text())
      dhigh = str(self.ui.lineEdit_11.text())
      pvar = str(self.ui.lineEdit_15.text())	
      cur.execute('INSERT INTO ctestdata VALUES(?,?,?,?,?)',(pclose,dlow,dhigh,pvar,riskcat))
      con.commit() 

  def csvcreate(self):
    os.system("python export1.py")
     
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
