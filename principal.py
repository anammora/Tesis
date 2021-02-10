import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow
from Ht import Ui_MainWindow

filename = "Horas.txt"

class Ht(QMainWindow):
    def __init__(self):
        super(Ht, self).__init__()
        self.readFile()
        try:

            self.ui = Ui_MainWindow()

            self.ui.setupUi(self)
            self.ui.dateTimeC1.dateTimeChanged.connect(self.Change2)
            self.ui.dateTimeC2.dateTimeChanged.connect(self.Change3)
            self.ui.dateTimeC3.dateTimeChanged.connect(self.Change4)
            self.ui.dateTimeC4.dateTimeChanged.connect(self.Change5)
            self.ui.dateTimeC5.dateTimeChanged.connect(self.Change6)
            self.ui.B_Save.clicked.connect(self.Save)
        except Exception as e:
                print(e)

    def Change2(self,CurrentDT):
        self.ui.dateTimeC2.setMinimumDateTime(CurrentDT)
    def Change3(self,CurrentDT):
        self.ui.dateTimeC3.setMinimumDateTime(CurrentDT)
    def Change4(self,CurrentDT):
        self.ui.dateTimeC4.setMinimumDateTime(CurrentDT)
    def Change5(self,CurrentDT):
        self.ui.dateTimeC5.setMinimumDateTime(CurrentDT)
    def Change6(self,CurrentDT):
        self.ui.dateTimeC6.setMinimumDateTime(CurrentDT)
    def Save(self):
        dateTimeC1=self.ui.dateTimeC1.dateTime()
        print(dateTimeC1.toString())
        self.ui.dateTimeC6.setMinimumDateTime(dateTimeC1)
        dateTimeC2=self.ui.dateTimeC2.dateTime()
        print(dateTimeC2.toString())
        dateTimeC3=self.ui.dateTimeC3.dateTime()
        print(dateTimeC3.toString())
        dateTimeC4=self.ui.dateTimeC4.dateTime()
        print(dateTimeC4.toString())
        dateTimeC5=self.ui.dateTimeC5.dateTime()
        print(dateTimeC5.toString())
        dateTimeC6=self.ui.dateTimeC6.dateTime()
        print(dateTimeC6.toString())
        
        
        fname = open(filename, 'w')
        fname.write(dateTimeC1.toString()+","+dateTimeC2.toString()
                    +","+dateTimeC3.toString()
                    +","+dateTimeC4.toString()+","+dateTimeC5.toString()
                    +","+dateTimeC6.toString())
        fname.close()
        
    def readFile(self):
        fname = open(filename, 'r')
        Horas= fname.read().split(',')
        dateTimeC1=QtCore.QDateTime.fromString(Horas[0],'yyyy/M/d hh:mm:ss')
        self.ui.dateTimeC1.setDateTimext(dateTimeC1)
        '''
        self.ui.dateTimeC2.setDateTimext(QtCore.QDateTime.fromString(Horas[1]))
        self.ui.dateTimeC3.setDateTimext(QtCore.QDateTime.fromString(Horas[2]))
        self.ui.dateTimeC4.setDateTimext(QtCore.QDateTime.fromString(Horas[3]))
        self.ui.dateTimeC5.setDateTimext(QtCore.QDateTime.fromString(Horas[4]))
        self.ui.dateTimeC6.setDateTimext(QtCore.QDateTime.fromString(Horas[5]))
        '''
        
    
#hola soy ana
app = QApplication([])

application = Ht()

application.show()

sys.exit(app.exec())

GPIO.cleanup()


