# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/TESIS/Inicio.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QThread, QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("IMG/cielo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 280, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.B_Emg = QtWidgets.QPushButton(self.centralwidget)
        self.B_Emg.setGeometry(QtCore.QRect(60, 200, 100, 100))
        self.B_Emg.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG/emergency-call.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Emg.setIcon(icon)
        self.B_Emg.setIconSize(QtCore.QSize(80, 80))
        self.B_Emg.setObjectName("B_Emg")
        self.B_Pill = QtWidgets.QPushButton(self.centralwidget)
        self.B_Pill.setGeometry(QtCore.QRect(540, 200, 100, 100))
        self.B_Pill.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("IMG/medicine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Pill.setIcon(icon1)
        self.B_Pill.setIconSize(QtCore.QSize(80, 80))
        self.B_Pill.setObjectName("B_Pill")
        self.B_Multimedia = QtWidgets.QPushButton(self.centralwidget)
        self.B_Multimedia.setGeometry(QtCore.QRect(300, 200, 100, 100))
        self.B_Multimedia.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("IMG/Multimedia.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Multimedia.setIcon(icon2)
        self.B_Multimedia.setIconSize(QtCore.QSize(80, 80))
        self.B_Multimedia.setObjectName("B_Multimedia")
        self.B_Settings = QtWidgets.QPushButton(self.centralwidget)
        self.B_Settings.setGeometry(QtCore.QRect(660, 0, 50, 50))
        self.B_Settings.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("IMG/technical-support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Settings.setIcon(icon3)
        self.B_Settings.setIconSize(QtCore.QSize(40, 40))
        self.B_Settings.setObjectName("B_Settings")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 180, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 180, 90, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 27))
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
        self.label_2.setText(_translate("MainWindow", "HOY ES : "+ QDate.currentDate().toString()))
        self.label_3.setText(_translate("MainWindow", "LA HORA ES: "+ QTime.currentTime().toString()))
        self.label_4.setText(_translate("MainWindow", "EMERGENCIA"))
        self.label_5.setText(_translate("MainWindow", "HORARIO DE TOMAS "))
        self.label_7.setText(_translate("MainWindow", "MULTIMEDIA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

