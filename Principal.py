import sys
import cv2
import time
import movMotor
import servito
#import subprocess
#import Reproductor
import push
import pygame
import ventanaEmergente
from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,pyqtSlot,QDate, QTime, QObject,QDateTime, Qt, QThread, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QApplication,QMainWindow,QPushButton
from PyQt5.QtGui import QImage,QPixmap
from Ht import Ui_MainWindow as Ui_Ht
from Remember import Ui_MainWindow as Ui_Remember
from setting import Ui_MainWindow as Ui_setting
from Inicio import Ui_MainWindow as Ui_Inicio
from Ht_pin import Ui_MainWindow as Ui_HtPin
from St_pin import Ui_MainWindow as Ui_StPin
#from playsound import playsound


exxit=0
filename = "Horas.txt"
filevideo="HVideo.txt"
PinFile="PinFile.txt"


class Worker(QObject):
    updHora=pyqtSignal()
    changePixmap = pyqtSignal(QImage)
    def __init__(self):
        super(Worker, self).__init__()
        self.Ht=Ht()
        self.setting=setting()
        self.Remember=Remember()
        self.Remember.ui.B_Close.clicked.connect(lambda:self.Remember.close())
        self.videoVentana=videoVentana()
    
    def run(self):
        ActServo1=QDateTime.currentDateTime()
        cap = cv2.VideoCapture('/media/pi/MORAMO/VIDEO(1)/abuela con Alzheimer reconoce.mp4')
        while True:
            try:
                
                self.updHora.emit()
                self.Ht.setDates()
                HoraVideo=self.setting.readFile()
                datetime = QDateTime.currentDateTime()
                #print(HoraVideo)
                #print(datetime.time().minute()) datetime.time().minute()==HoraVideo[1]
                #print(int(HoraVideo[0]))
                if (int(datetime.time().hour())==int(HoraVideo[0])):
                    ret, frame = cap.read()
                    #print(ret)
                    #print('entra')
                    #self.video(frame,ret)

                    #time.sleep(60) 
                    
                            
                if (datetime.date()==self.Ht.ui.dateTimeC1.date()and
                datetime.time().hour()==self.Ht.ui.dateTimeC1.time().hour()and
                datetime.time().minute()==self.Ht.ui.dateTimeC1.time().minute()and
                datetime.time().second()==self.Ht.ui.dateTimeC1.time().second()):
                    #print('yes')
                    #movMotor.run()
                    self.Remember.show()
                    pygame.mixer.init()
                    pygame.mixer.music.load("/home/pi/Music/alarm-clock.mp3")
                    pygame.mixer.music.play()
                    ActServo1=datetime.addSecs(30)
                    print(ActServo1)
                    #time.sleep(60)
                    
                if (datetime.date()==ActServo1.date()and
                datetime.time().hour()==ActServo1.time().hour()and
                datetime.time().minute()==ActServo1.time().minute()and
                datetime.time().second()==ActServo1.time().second()):
                    
                    print('yes')
                    servito.run()
                    #time.sleep(60)
                    
                
                #print(datetime.addSecs(120).toString(Qt.ISODate))  
            except Exception as e:
                print(e)
    def video(self,frame,ret):
        
        rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)
        frame=cv2.resize(frame,(800,480))
        if ret==False:
            print('aqui esta')
            frame=cv2.resize(frame,(0,0))  
        #cv2.imshow('VIDEO',frame)
        #cap.release()   
        #cv2.destroyAllWindows()
        
            
class Inicio(QMainWindow):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self)
        #self.label = QLabel(self)
        #self.label.move(30, 0)
        #self.label.resize(800, 480)
  
        try:

            self.ui.B_Pill.clicked.connect(self.create_HtPin_window)
            self.ui.B_Settings.clicked.connect(self.create_StPin_window)
            #self.ui.B_Pill.clicked.connect(lambda:self.close())
            self.thread=QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.thread.start()
            self.worker.updHora.connect(self.updateLabel)
            #self.worker.changePixmap.connect(self.setImage)
            #self.ui.B_Music.clicked.connect(Reproductor.run)
            self.ui.B_Multimedia.clicked.connect(self.openMultimedia)
            self.ui.B_Emg.clicked.connect(push.run)
            
        except Exception as e:
            print(e)
            
    def create_Ht_window(self):
        self.Ht=Ht()
        self.Ht.show()
        
    def create_HtPin_window(self):
        
        self.Ht_pin=Ht_pin()
        self.Ht_pin.show()
    def create_StPin_window(self):
        
        self.St_pin=St_pin()
        self.St_pin.show()
        
    def updateLabel(self):
        self.ui.label_3.setText("LA HORA ES: "+ QTime.currentTime().toString())
        self.ui.label_2.setText("HOY ES : "+ QDate.currentDate().toString())
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))   
    def openMultimedia(self):
        ventanaEmergente.run()
    
class videoVentana(QWidget):
    def __init__(self):
        super(videoVentana, self).__init__()
        self.title = "PyQt4 Video"
        self.left = 0
        self.top = 0
        self.width = 400
        self.height = 480
        self.initUI()
        

    
    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # create a label
        self.label = QLabel(self)
        self.label.move(280, 120)
        self.label.resize(800, 480)
          
           
        
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
        
class St_pin(QMainWindow):
    def __init__(self):
        super(St_pin, self).__init__()
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
            self.create_setting_window()
            
        else:
            self.label.setText("La clave es incorrecta")
            self.ui.lineEdit.clear()
            
            
    def create_setting_window(self):
        
        self.setting=setting()
        self.setting.show()
        
    def create_Inicio_window(self):
        self.Inicio=Inicio()
        self.Inicio.show()
        
class Remember(QMainWindow):
    def __init__(self):
        super(Remember, self).__init__()
        self.ui = Ui_Remember()

        self.ui.setupUi(self)
        
        try:
            
            self.ui.B_Close.clicked.connect(self.close())
        except Exception as e:
            print(e)
            
class setting(QMainWindow):
    def __init__(self):
        global HoraVideo 
        super(setting, self).__init__()
        self.ui = Ui_setting()

        self.ui.setupUi(self)
        HoraVideo=self.readFile()
        #print(HoraVideo)
        try:
            self.ui.B_Save.clicked.connect(self.Save)
            self.ui.B_Home.clicked.connect(lambda:self.close())
            
            
        except Exception as e:
            print(e)
            
    def Save(self):
        timeEditVideo=self.ui.timeEditVideo.time()
        fname = open(filevideo, 'w')
        fname.write(timeEditVideo.toString(Qt.ISODate))
        fname.close()
    def readFile(self):
        fname = open(filevideo, 'r')
        HoraVideo= fname.read().split(':')
        #print(Horas)
        return HoraVideo
        
            
class Ht(QMainWindow):
    def __init__(self):
        super(Ht, self).__init__()
        self.ui = Ui_Ht()

        self.ui.setupUi(self)
        Horas=self.readFile()
        try:

            #self.ui.dateTimeC1.setMinimumDateTime(QDateTime.currentDateTime())
            self.ui.dateTimeC1.dateTimeChanged.connect(self.Change2)
            self.ui.dateTimeC2.dateTimeChanged.connect(self.Change3)
            self.ui.dateTimeC3.dateTimeChanged.connect(self.Change4)
            self.ui.dateTimeC4.dateTimeChanged.connect(self.Change5)
            self.ui.dateTimeC5.dateTimeChanged.connect(self.Change6)
            
            self.ui.B_Save.clicked.connect(self.Save)
            
            self.setDates()
            
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
        #print(Horas)
        return Horas
        
    def setDates(self):
        Horas=self.readFile()
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



