# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/TESIS/setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(600, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.timeEditVideo = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEditVideo.setGeometry(QtCore.QRect(150, 130, 118, 32))
        self.timeEditVideo.setAcceptDrops(False)
        self.timeEditVideo.setWrapping(False)
        self.timeEditVideo.setFrame(True)
        self.timeEditVideo.setKeyboardTracking(False)
        self.timeEditVideo.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEditVideo.setCalendarPopup(False)
        self.timeEditVideo.setObjectName("timeEditVideo")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(150, 40, 113, 32))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.B_Home = QtWidgets.QPushButton(self.centralwidget)
        self.B_Home.setGeometry(QtCore.QRect(550, 0, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Tibetan")
        self.B_Home.setFont(font)
        self.B_Home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_Home.setIcon(icon)
        self.B_Home.setIconSize(QtCore.QSize(40, 40))
        self.B_Home.setObjectName("B_Home")
        self.B_Save = QtWidgets.QPushButton(self.centralwidget)
        self.B_Save.setGeometry(QtCore.QRect(270, 190, 99, 30))
        self.B_Save.setObjectName("B_Save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 28))
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
        self.label_2.setText(_translate("MainWindow", "CONFIGURACIÓN"))
        self.label_3.setText(_translate("MainWindow", "CAMBIAR CLAVE"))
        self.label_4.setText(_translate("MainWindow", "HORA DE REPRODUCCIÓN DEL VIDEO"))
        self.B_Save.setText(_translate("MainWindow", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

