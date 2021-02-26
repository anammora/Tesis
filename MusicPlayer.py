# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Music.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import (QAbstractVideoBuffer, QMediaContent,
        QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)

from PyQt5.QtWidgets import (QWidget,QApplication,QPushButton,
                             QVBoxLayout,QFileDialog,QHBoxLayout)

import pygame  
                                                   # +++
pygame.mixer.init()

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("IMG/CASSETE.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.B_Sound = QtWidgets.QPushButton(self.centralwidget)
        self.B_Sound.setGeometry(QtCore.QRect(280, 270, 110, 110))
        self.B_Sound.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG/volume-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Sound.setIcon(icon)
        self.B_Sound.setIconSize(QtCore.QSize(90, 90))
        self.B_Sound.setObjectName("B_Sound")
        self.B_Play = QtWidgets.QPushButton(self.centralwidget)
        self.B_Play.setGeometry(QtCore.QRect(40, 270, 110, 110))
        self.B_Play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("IMG/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Play.setIcon(icon1)
        self.B_Play.setIconSize(QtCore.QSize(90, 90))
        self.B_Play.setObjectName("B_Play")
        self.B_Pause = QtWidgets.QPushButton(self.centralwidget)
        self.B_Pause.setGeometry(QtCore.QRect(160, 270, 110, 110))
        self.B_Pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("IMG/pause-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Pause.setIcon(icon2)
        self.B_Pause.setIconSize(QtCore.QSize(90, 90))
        self.B_Pause.setObjectName("B_Pause")
        self.B_NoSound = QtWidgets.QPushButton(self.centralwidget)
        self.B_NoSound.setGeometry(QtCore.QRect(400, 270, 110, 110))
        self.B_NoSound.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("IMG/no-sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_NoSound.setIcon(icon3)
        self.B_NoSound.setIconSize(QtCore.QSize(90, 90))
        self.B_NoSound.setObjectName("B_NoSound")
        self.B_Back = QtWidgets.QPushButton(self.centralwidget)
        self.B_Back.setGeometry(QtCore.QRect(520, 270, 110, 110))
        self.B_Back.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("IMG/rewind-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Back.setIcon(icon4)
        self.B_Back.setIconSize(QtCore.QSize(90, 90))
        self.B_Back.setObjectName("B_Back")
        self.B_Next = QtWidgets.QPushButton(self.centralwidget)
        self.B_Next.setGeometry(QtCore.QRect(640, 270, 110, 110))
        self.B_Next.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("IMG/forward-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Next.setIcon(icon5)
        self.B_Next.setIconSize(QtCore.QSize(90, 90))
        self.B_Next.setObjectName("B_Next")
        self.B_Home = QtWidgets.QPushButton(self.centralwidget)
        self.B_Home.setGeometry(QtCore.QRect(730, 0, 70, 70))
        self.B_Home.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("IMG/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Home.setIcon(icon6)
        self.B_Home.setIconSize(QtCore.QSize(60, 60))
        self.B_Home.setObjectName("B_Home")
        self.SongName = QtWidgets.QLabel(self.centralwidget)
        self.SongName.setGeometry(QtCore.QRect(40, 120, 701, 51))
        self.SongName.setText("")
        self.SongName.setObjectName("SongName")
        self.label.raise_()
        self.B_Sound.raise_()
        self.B_Play.raise_()
        self.B_Pause.raise_()
        self.B_NoSound.raise_()
        self.B_Back.raise_()
        self.B_Next.raise_()
        self.label_2.raise_()
        self.B_Home.raise_()
        self.SongName.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "MUSICA"))
        self.B_Home.clicked.connect(self.anadir)
        #self.B_Pause.clicked.connect(self.setState)            
        self.B_Play.clicked.connect(self.setState)
        
    

    def anadir(self):
        
        cancion= QFileDialog.getOpenFileName(self,
                                              str('Open'),
                                              str('/media/pi/MORAMO/MUSICA/'),
                                              str('Music(*.mp3)'))
        self.data = cancion[0]
        
      
    def setState(self,state):
        self.B_Play=pygame.mixer.init()  
        pygame.mixer.music.load(self.data)
        #pygame.mixer.music.load("/media/pi/MORAMO/MUSICA/Camilo-Ropa Cara.mp3")
        pygame.mixer.music.play(loops=0)
        #icon7 = QtGui.QIcon()
        #icon7.addPixmap(QtGui.QPixmap("IMG/pause-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.B_Play.setIcon(icon7)
        

'''        
        if self.B_Play is None:
            self.B_Play.setIcon(QtGui.QIcon( QtGui.QPixmap("IMG/pause-button.png")))
            self.B_Play = "pause"
            pygame.mixer.music.pause()
        else:
            self.B_Play.setIcon(QIcon("IMG/play.png"))
            self.B_Play =None
            pygame.mixer.music.unpause()
        
'''

if __name__ == "__main__":
    import sys,os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
