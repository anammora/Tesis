# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/TESIS/St_pin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("IMG/cielo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 160, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.B_Loggin = QtWidgets.QPushButton(self.centralwidget)
        self.B_Loggin.setGeometry(QtCore.QRect(340, 270, 81, 31))
        self.B_Loggin.setObjectName("B_Loggin")
        self.B_Home = QtWidgets.QPushButton(self.centralwidget)
        self.B_Home.setGeometry(QtCore.QRect(750, 0, 50, 50))
        self.B_Home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Home.setIcon(icon)
        self.B_Home.setIconSize(QtCore.QSize(40, 40))
        self.B_Home.setObjectName("B_Home")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 220, 113, 32))
        self.lineEdit.setObjectName("lineEdit")
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
        self.label_2.setText(_translate("MainWindow", "HORARIOS DE TOMA "))
        self.label_3.setText(_translate("MainWindow", "INGRESA EL PIN "))
        self.B_Loggin.setText(_translate("MainWindow", "Ingresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

