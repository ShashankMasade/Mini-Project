import sys
import csv
import os
from export import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('sqlite/eqre1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'eqre1'); 

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.traincsv)
     self.ui.pushButton_2.clicked.connect(self.testcsv)
     self.ui.pushButton_3.clicked.connect(self.ctestcsv)
     self.ui.pushButton_4.clicked.connect(self.filelocs)

  def testcsv(self):
    with con:
      cur = con.cursor()
      cur.execute('SELECT * FROM testdata;')
      rows = cur.fetchall()
      fp = open('test1.csv', 'w')
      myFile = csv.writer(fp)
      myFile.writerows(rows)
      fp.close()
      con.commit()

  def traincsv(self):
    with con:
      cur = con.cursor()
      cur.execute('SELECT * FROM traindata;')
      rows = cur.fetchall()
      fp = open('train1.csv', 'w')
      myFile = csv.writer(fp)
      myFile.writerows(rows)
      fp.close()
      con.commit()

  def ctestcsv(self):
    with con:
      cur = con.cursor()
      cur.execute('SELECT * FROM ctestdata;')
      rows = cur.fetchall()
      fp = open('ctest1.csv', 'w')
      myFile = csv.writer(fp)
      myFile.writerows(rows)
      fp.close()
      con.commit()

  def filelocs(self):
    os.system("python exectensor1.py")
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
