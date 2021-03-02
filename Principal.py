import sys
import time
import Reproductor
import pygame
#import VisorImg

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QObject,QDateTime, Qt, QThread, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow,QPushButton
from Ht import Ui_MainWindow as Ui_Ht
from Remember import Ui_MainWindow as Ui_Remember
from Inicio import Ui_MainWindow as Ui_Inicio
from Ht_pin import Ui_MainWindow as Ui_HtPin
from playsound import playsound


exxit=0
filename = "Horas.txt"
PinFile="PinFile.txt"


class Worker(QObject):
    def __init__(self):
        super(Worker, self).__init__()
        self.Ht=Ht()
        self.Remember=Remember()
        self.Remember.ui.B_Close.clicked.connect(lambda:self.Remember.close())
    
    def run(self):       
        while True:
            try:
                
                datetime = QDateTime.currentDateTime()
                #print('curenttime '+ str(datetime.date())+' '+str(datetime.time().hour())+' '+
                      #str(datetime.time().minute())+' C1 '+str(self.Ht.ui.dateTimeC1.date())+' '+
                      #str(self.Ht.ui.dateTimeC1.time().hour())+' '+
                      #str(self.Ht.ui.dateTimeC1.time().minute()))
                if (datetime.date()==self.Ht.ui.dateTimeC1.date()and
                datetime.time().hour()==self.Ht.ui.dateTimeC1.time().hour()and
                datetime.time().minute()==self.Ht.ui.dateTimeC1.time().minute()):
                    
                    print('yes')
                    #playsound('/home/pi/Music/alarm-clock.mp3')
                    self.Remember.show()
                    pygame.mixer.init()
                    pygame.mixer.music.load("/home/pi/Music/alarm-clock.mp3")
                    pygame.mixer.music.play()
                    #playsound('/home/pi/Music/alarm-clock.mp3')
                    #MOTOR
                    time.sleep(60)
               
            except Exception as e:
                print(e)
            
         
        
                    
class Inicio(QMainWindow):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self)
  
        try:

            self.ui.B_Pill.clicked.connect(self.create_HtPin_window)
            #self.ui.B_Pill.clicked.connect(lambda:self.close())
            self.thread=QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.thread.start()
            self.ui.B_Music.clicked.connect(Reproductor.run)
            #self.ui.B_Photo.clicked.connect(VisorImg.runn)
            
            
        except Exception as e:
            print(e)
            
    def create_Ht_window(self):
        
        self.Ht=Ht()
        self.Ht.show()
        
    def create_HtPin_window(self):
        
        self.Ht_pin=Ht_pin()
        self.Ht_pin.show()
        
class Ht_pin(QMainWindow):
    def __init__(self):
        super(Ht_pin, self).__init__()
        self.ui = Ui_HtPin()

        self.ui.setupUi(self)
        self.label = QLabel("",self)
        self.label.setGeometry(340, 300, 200, 25)
        self.ui.B_Loggin.clicked.connect(lambda:self.Compare())
        #self.ui.B_Home.clicked.connect(self.create_Inicio_window)
        self.ui.B_Home.clicked.connect(lambda:self.close())
        
    def Compare(self):
        fname = open(PinFile, 'r')
        Pin= fname.read()
        print(Pin)
        if str(self.ui.lineEdit.text())==Pin:
            #print('otra vez este hpta')
            self.close()
            self.create_Ht_window()
            
        else:
            self.label.setText("La clave es incorrecta")
            self.ui.lineEdit.clear()
            
            
    def create_Ht_window(self):
        
        self.Ht=Ht()
        self.Ht.show()
        
    def create_Inicio_window(self):
        self.Inicio=Inicio()
        self.Inicio.show()
        
class Remember(QMainWindow):
    def __init__(self):
        super(Remember, self).__init__()
        self.ui = Ui_Remember()

        self.ui.setupUi(self)
        
        try:
            #print('hpta')
            
            self.ui.B_Close.clicked.connect(self.close())
        except Exception as e:
            print(e)
            
        
class Ht(QMainWindow):
    def __init__(self):
        super(Ht, self).__init__()
        self.ui = Ui_Ht()

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
            #self.setDates(Horas)
            
            
            #self.ui.B_Home.clicked.connect(self.create_Inicio_window)
            self.ui.B_Home.clicked.connect(lambda:self.close())
            
            
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
    


app = QApplication([])

application = Inicio()

application.show()

sys.exit(app.exec())

GPIO.cleanup()



