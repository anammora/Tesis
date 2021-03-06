import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QThread, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow,QPushButton
from Ht import Ui_MainWindow
from Remember import Ui_MainWindow as Ui_Remember
from Inicio import Ui_MainWindow as Ui_Inicio

filename = "Horas.txt"
Compare=False

class Remember(QMainWindow):
    def __init__(self):
        super(Remember, self).__init__()
        self.ui = Ui_Remember()
        self.ui.setupUi(self)

class Thread(QThread):
    
    def __init__(self):
        super(Thread, self).__init__()
        self.ui=ui
        
    def run(self):
        self.Ht=Ht()
        print (Ht())
        while True:
            try:
                datetime = QDateTime.currentDateTime()
                
                if (datetime.date()==Ht().dateTimeC1.date()and
                datetime.time().hour()==Ht().dateTimeC1.time().hour()and
                datetime.time().minute()==Ht().dateTimeC1.time().minute()):
                    
                    self.Remember().show()
                    #self.create_Remember_window
                    print('yes')
                    
            except Exception as e:
                print(e)
    def create_Ht_window(self):
        
        self.Ht=Ht()
        
    #def create_Remember_window(self):
    #    self.Rem = Remember()
    #    RemWindow=self.Rem.show()
          
class Inicio(QMainWindow):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self)
  
        try:

            self.ui.B_Pill.clicked.connect(self.create_Ht_window)
            self.ui.B_Pill.clicked.connect(lambda:self.close())
            
        except Exception as e:
            print(e)
            
    def create_Ht_window(self):
        
        self.Ht=Ht()
        self.Ht.show()
            
   
class Ht(QMainWindow):
    def __init__(self):
        super(Ht, self).__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        Horas=self.readFile()
        try:

            self.ui.dateTimeC1.setMinimumDateTime(QDateTime.currentDateTime())
            self.ui.dateTimeC1.dateTimeChanged.connect(self.Change2)
            self.ui.dateTimeC2.dateTimeChanged.connect(self.Change3)
            self.ui.dateTimeC3.dateTimeChanged.connect(self.Change4)
            self.ui.dateTimeC4.dateTimeChanged.connect(self.Change5)
            self.ui.dateTimeC5.dateTimeChanged.connect(self.Change6)
            
            self.ui.B_Save.clicked.connect(self.Save)
            self.setDates(Horas)
            
            self.ui.B_Home.clicked.connect(self.create_Inicio_window)
            self.ui.B_Home.clicked.connect(lambda:self.close())
                   
            #self.thread=Thread(self.ui)
            #self.thread.start()
            #self.th=QThread(self)
            #self.thread.moveToThread(self.th)
            
            
        except Exception as e:
                print(e)
                
    def create_Inicio_window(self):
        self.Inicio=Inicio()
        self.Inicio.show()

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
        #print(dateTimeC1.toString())
        dateTimeC2=self.ui.dateTimeC2.dateTime()
        dateTimeC3=self.ui.dateTimeC3.dateTime()
        dateTimeC4=self.ui.dateTimeC4.dateTime()
        dateTimeC5=self.ui.dateTimeC5.dateTime()
        dateTimeC6=self.ui.dateTimeC6.dateTime()
        
        
        fname = open(filename, 'w')
        fname.write(dateTimeC1.toString(Qt.ISODate)+","+dateTimeC2.toString(Qt.ISODate)
                    +","+dateTimeC3.toString(Qt.ISODate)
                    +","+dateTimeC4.toString(Qt.ISODate)+","+dateTimeC5.toString(Qt.ISODate)
                    +","+dateTimeC6.toString(Qt.ISODate))
        fname.close()
        
    def readFile(self):
        fname = open(filename, 'r')
        Horas= fname.read().split(',')
        return Horas
        
    def setDates(self,Horas):
        
        dateTime1=QtCore.QDateTime.fromString(Horas[0],Qt.ISODate)
        self.ui.dateTimeC1.setDateTime(dateTime1)
        
        dateTime2=QtCore.QDateTime.fromString(Horas[1],Qt.ISODate)
        self.ui.dateTimeC2.setDateTime(dateTime2)
        
        dateTime3=QtCore.QDateTime.fromString(Horas[2],Qt.ISODate)
        self.ui.dateTimeC3.setDateTime(dateTime3)
        
        dateTime4=QtCore.QDateTime.fromString(Horas[3],Qt.ISODate)
        self.ui.dateTimeC4.setDateTime(dateTime4)
        
        dateTime5=QtCore.QDateTime.fromString(Horas[4],Qt.ISODate)
        self.ui.dateTimeC5.setDateTime(dateTime5)
        
        dateTime6=QtCore.QDateTime.fromString(Horas[5],Qt.ISODate)
        self.ui.dateTimeC6.setDateTime(dateTime6)
        
def readDateTime():
        fname = open(filename, 'r')
        DateTime= fname.read().split(',')
        return DateTime
    
def CompareDateTime(DateTime):
    dateTime1=QtCore.QDateTime.fromString(DateTime[0],Qt.ISODate)
    dateTime2=QtCore.QDateTime.fromString(DateTime[1],Qt.ISODate)
    dateTime3=QtCore.QDateTime.fromString(DateTime[2],Qt.ISODate)
    dateTime4=QtCore.QDateTime.fromString(DateTime[3],Qt.ISODate)
    dateTime5=QtCore.QDateTime.fromString(DateTime[4],Qt.ISODate)
    dateTime6=QtCore.QDateTime.fromString(DateTime[5],Qt.ISODate)
    datetimeCurrent = QDateTime.currentDateTime()
    
    if (datetimeCurrent.date()==dateTime1.date()and
    datetimeCurrent.time().hour()==dateTime1.time().hour()and
    datetimeCurrent.time().minute()==dateTime1.time().minute()):
        Compare=True
    else:
        Compare=False            
                
    return Compare 
     
        
        
    
if __name__ == '__main__':
    
    app = QApplication([])

    application = Inicio()
    
    application.show()

    #thread=Thread()
    
    #thread.start()

    DateTime=readDateTime()
    print(CompareDateTime(DateTime))
    
    while True:
        
        try:
            application.show()
        
            
            #if CompareDateTime(DateTime):
                    #Remember().show()
                
            print('hello')
        except Exception as e:
                print(e) 
            
                    
    
            
    sys.exit(app.exec())
    
    

    #GPIO.cleanup()
