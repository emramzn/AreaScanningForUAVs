# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:53:37 2020

@author: 90538
"""

import PyQt5
import numpy as np
import pymap
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QPainter, QBrush, QPen,QFont
from PyQt5.QtWidgets import QMainWindow,QGroupBox, QApplication,QVBoxLayout, QComboBox,QListWidgetItem , QSizePolicy,QListWidget, QGridLayout, QWidget, QDesktopWidget, QPushButton, QAction, QLineEdit, QMessageBox ,QLabel, QProgressBar

from matplotlib import colors
from PyQt5.QtCore import Qt

#    
# %%


import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Path Planning For UAVs'
        self.left = 10
        self.top = 10
        self.width = 1600
        self.height = 1500
        self.setWindowIcon(QIcon('windowicon.png'))
        self.setStyleSheet("QPushButton {\n"
"background-color:#347deb;\n"
"border-radius:10px;\n"
"color:white;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:pressed   {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:14px;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"border:none;\n"
"padding: 0 8px;\n"
"}\n"




"QLineEdit::hover{\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
"border-radius:10px;\n"
"border:none;\n"
"background-color:#bcbcbc;\n"
"color:black;\n"
"}\n"
"\n"
"QCheckBox{\n"
"spacing:5px;\n"
"\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 23px;\n"
"    height: 23px;\n"
"}\n"
"\n"
"")     
    
        self.initUI()
  


    def imag(self):
        self.l1.setPixmap(QPixmap("mapsPY.png"))
   
    
    def importDraw(self,lat,lng,typeMap):
      pymap.DrawGrid(self,float(lng),float(lng))    
      self.l1.setPixmap(QPixmap("myImageGrid.png"))
               
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.blue)
        
        painter.drawLine(20,280,280,280)
        painter.drawLine(20,550,280,550)
        painter.drawLine(20,75,280,75)
     
    
    def appendFunc(self):
        self.Txt_points.setText("lat:40.2531640 , lng: 29.251355 \n")

    def initUI(self):
       
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        

        self.l1 =  QLabel(self)
        self.l1.setPixmap(QPixmap("screen.jpg"))
        self.l1.setGeometry(450,5,1000,1000)
        
        self.swtPixmap =  QLabel(self)
        self.swtPixmap.setPixmap(QPixmap("swtPixmap.png"))
        self.swtPixmap.setGeometry(40,700,260,260)
        
        self.label=QLabel("Routa Planning For UAVs",self)
        self.label.move(70,860)
        self.label.resize(250,150)
        self.label.setFont(QFont('Arial', 12))
        
        self.labelCount=QLabel(self)
        self.labelCount.move(60,2)
        self.labelCount.resize(200,100)
        self.labelCount.setFont(QFont('SansSerif', 18))
        
        
#%% Maps Features  
     
        #Title
        self.label=QLabel("Map Features",self)
        self.label.move(25,510)
        self.label.resize(250,45)
        self.label.setFont(QFont('Arial', 14)) 
        
        #ComboBox Label
        self.label=QLabel("Type Of Map",self)
        self.label.move(50,560)
        self.label.resize(150,25)
        
        ## Combo Box
        self.combo =QComboBox(self)
        self.combo.addItem("Hybrid")
        self.combo.addItem("Sattelite")
        self.combo.addItem("Terrain")
        self.combo.setStyleSheet("QComboBox {background-color: white;border-style: outset; border-width: 2px;border-radius: 5px;border-color: #448aff; font:  12px; min-width: 10em; padding: 3px;}")
        self.combo.move(50, 590)

        #Button
        self.TypeBtn = QPushButton('Loc', self)
        self.TypeBtn.move(240,585)
        self.TypeBtn.resize(40,40)
        self.TypeBtn.clicked.connect(lambda:self.appendFunc())
                
        
        
        
        
 #%%    Location Features   
        
        self.label=QLabel("Latitude",self)
        self.label.move(50,100)
        self.label.resize(150,25)

        self.label=QLabel("Longitude",self)
        self.label.move(50,150)
        self.label.resize(150,25)
        
        self.label=QLabel("Location Features",self)
        self.label.setFont(QFont('Arial', 14)) 
        self.label.move(25,10)
        self.label.resize(250,100)

        self.lng=QLineEdit(self)
        self.lng.move(50,120)
        self.lng.resize(180,25)
        

        self.lat=QLineEdit(self)
        self.lat.move(50,170)
        self.lat.resize(180,25)
        
        self.btnadd = QPushButton('Loc', self)
        self.btnadd.move(245,120)
        self.btnadd.resize(40,75)
        self.btnadd.clicked.connect(lambda:self.appendFunc())
        
        self.btnadd = QPushButton('Map', self)
        self.btnadd.move(50,210)
        self.btnadd.resize(85,40)
        self.btnadd.clicked.connect(lambda:self.imag())
        
        self.btnadd = QPushButton('Draw Grid', self)
        self.btnadd.move(150,210)
        self.btnadd.resize(85,40)
        self.btnadd.clicked.connect(lambda:self.importDraw(self.lat.text(),self.lng.text(),self.combo.currentText() ))
                
        self.Txt_points=QLineEdit(self)
        self.Txt_points.move(50,300)
        self.Txt_points.resize(200,200)
       
        self.show()
        
 
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    
    sys.exit(app.exec_())
