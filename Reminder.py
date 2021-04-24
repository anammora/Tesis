# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reminder.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Bassa Vah")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.B_Close = QtWidgets.QPushButton(self.centralwidget)
        self.B_Close.setGeometry(QtCore.QRect(140, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_Close.setFont(font)
        self.B_Close.setObjectName("B_Close")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Bassa Vah")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 71, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("IMG/reminder.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 81, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("IMG/drug.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 27))
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
        self.label.setText(_translate("MainWindow", "ES HORA DE TOMAR  "))
        self.B_Close.setText(_translate("MainWindow", "CERRAR"))
        self.label_2.setText(_translate("MainWindow", "TUS PASTILLAS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

