import sys
import time
import RPi.GPIO as GPIO
import pygame
import os
import cv2
import movMotor
import servito
import push
import ventanaEmergente
from tkinter import *

#import VisorImg

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QUrl,pyqtSlot,QDate, QTime, QObject,QDateTime, Qt, QThread, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QApplication,QMainWindow,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from Ht import Ui_MainWindow as Ui_Ht
from Reminder import Ui_MainWindow as Ui_Reminder
from RechargeReminder import Ui_MainWindow as Ui_RechargeReminder
from setting import Ui_MainWindow as Ui_setting
from Inicio import Ui_MainWindow as Ui_Inicio
from Ht_pin import Ui_MainWindow as Ui_HtPin
#from VideoCap import Ui_MainWindow as Ui_VideoCap


exxit=0
filename = "Horas.txt"
filevideo="HVideo.txt"
PinFile="PinFile.txt"

VIDEO_PATH = "/media/pi/MORAMO/VIDEO(1)/AnimalesTiernos.mp4"
video = cv2.VideoCapture(VIDEO_PATH)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
duration = frame_count/fps
global signal
signal=True

#clip = VideoFileClip(VIDEO_PATH)
#print( clip.duration )

class Worker(QObject):
    updHora=pyqtSignal()
    def __init__(self):
        super(Worker, self).__init__()
        self.Ht=Ht()
        self.setting=setting()
        self.Reminder=Reminder()
        self.Reminder.ui.B_Close.clicked.connect(lambda:self.Reminder.close())
        self.RechargeReminder=RechargeReminder()
        self.RechargeReminder.ui.B_Close.clicked.connect(lambda:self.RechargeReminder.close())
        #GPIO.setmode(GPIO.BCM)
    
    def run(self):
        ActServo= QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0))
        ActC7= QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0))
        while True:
            try:
                self.updHora.emit()
                self.Ht.setDates()
                datetime = QDateTime.currentDateTime()
                #HoraVideo=self.setting.readFile()
                #print(duration)
                condicionC1= (datetime.date()==self.Ht.ui.dateTimeC1.date()and
                    datetime.time().hour()==self.Ht.ui.dateTimeC1.time().hour()and
                    datetime.time().minute()==self.Ht.ui.dateTimeC1.time().minute()and#):#and
                    datetime.time().second()==self.Ht.ui.dateTimeC1.time().second())

                if (condicionC1)or\
                (datetime.date()==self.Ht.ui.dateTimeC2.date()and
                datetime.time().hour()==self.Ht.ui.dateTimeC2.time().hour()and
                datetime.time().minute()==self.Ht.ui.dateTimeC2.time().minute()and#):#and
                datetime.time().second()==self.Ht.ui.dateTimeC2.time().second()):
                    
                    ActServo=self.ActDispense(datetime)
                    
                if (datetime.date()==self.Ht.ui.dateTimeC6.date()and
                datetime.time().hour()==self.Ht.ui.dateTimeC6.time().hour()and
                datetime.time().minute()==self.Ht.ui.dateTimeC6.time().minute()and#):#and
                datetime.time().second()==self.Ht.ui.dateTimeC6.time().second()):
                    
                    ActServo=self.ActDispense(datetime)
                    ActC7=datetime.addSecs(60)#3600
                    print(ActC7)
                
                if (datetime.date()==ActServo.date()and
                datetime.time().hour()==ActServo.time().hour()and
                datetime.time().minute()==ActServo.time().minute()and
                datetime.time().second()==ActServo.time().second()):
                    
                    print('yes claro')
                    servito.run()
                    
                    #time.sleep(10)
                if (datetime.date()==ActC7.date()and
                datetime.time().hour()==ActC7.time().hour()and
                datetime.time().minute()==ActC7.time().minute()and
                datetime.time().second()==ActC7.time().second()):
                    
                    print('Compartimento7')
                    movMotor.run()
                    self.RechargeReminder.show()
                    # Mostrar pantalla de cargar 
                    #time.sleep(10)
                
                
                #GPIO.cleanup()                    
            except Exception as e:
                print(e)
    def ActDispense(self,datetime):
        
        print('yes')
        movMotor.run()
        #time.sleep(2)
        self.Reminder.show()
        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Music/alarm-clock.mp3")
        pygame.mixer.music.play()
        ActServo=datetime.addSecs(30)
        print(ActServo)
        time.sleep(10)
        return ActServo

class WorkerVideo(QObject):
    
    def __init__(self):
        super(WorkerVideo, self).__init__()
        self.VideoCap=VideoCap()
        self.setting=setting()
        #self.videoVentana=videoVentana()'
        global signal
 
    def run(self):
        signal=True 
        while signal:
            
            try:
                               
                datetime = QDateTime.currentDateTime()
                HoraVideo=self.setting.readFile()
                #print(duration)
                #print(int(datetime.time().minute()),int(HoraVideo[1]) )   
                if (int(datetime.time().hour())==int(HoraVideo[0]) and\
                    int(datetime.time().minute())==int(HoraVideo[1])):
                    
                    #print("entra")
                    self.VideoCap.show()
                    time.sleep(duration+2)
                    signal=False
                
                if (signal==False) :
                    self.VideoCap.close()
                 
            except Exception as e:
                print(e)
        
            
class Inicio(QMainWindow):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self)

        try:

            self.ui.B_Pill.clicked.connect(lambda:self.create_HtPin_window('HT'))
            self.ui.B_Settings.clicked.connect(lambda:self.create_HtPin_window('ST'))
            #self.ui.B_Pill.clicked.connect(lambda:self.close())
            self.thread=QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.thread.start()
            
            self.thread1=QThread()
            self.WorkerVideo = WorkerVideo()
            self.WorkerVideo.moveToThread(self.thread1)
            self.thread1.started.connect(self.WorkerVideo.run)
            self.thread1.start()
            

            self.worker.updHora.connect(self.updateLabel)
            self.ui.B_Multimedia.clicked.connect(self.openMultimedia)
            self.ui.B_Emg.clicked.connect(push.run)
            
        except Exception as e:
            print(e)
            
    def create_Ht_window(self):
        self.Ht=Ht()
        self.Ht.show()
        
    def create_HtPin_window(self,var):
        print(var)
        self.Ht_pin=Ht_pin(var)
        self.Ht_pin.show()
       
    def updateLabel(self):
        self.ui.label_3.setText("LA HORA ES: "+ QTime.currentTime().toString())
        self.ui.label_2.setText("HOY ES : "+ QDate.currentDate().toString())
      
    def openMultimedia(self):
        ventanaEmergente.run()
      
class Ht_pin(QMainWindow):
    def __init__(self,var):
        super(Ht_pin, self).__init__()
        self.ui = Ui_HtPin()

        self.ui.setupUi(self)
        self.label = QLabel("",self)
        self.label.setGeometry(340, 300, 200, 25)
        self.var=var
        self.ui.B_Loggin.clicked.connect(lambda:self.Compare(var))
        #self.ui.B_Home.clicked.connect(self.create_Inicio_window)
        self.ui.B_Home.clicked.connect(lambda:self.close())
        
    def Compare(self,var):
        fname = open(PinFile, 'r')
        Pin= fname.read()
        print(Pin)
        if str(self.ui.lineEdit.text())==str(Pin):
            #print('otra vez este hpta')
            if var=='HT':
                self.close()
                self.create_Ht_window()
            else:
                self.close()
                self.create_St_window()
            
        else:
            self.label.setText("La clave es incorrecta")
            self.ui.lineEdit.clear()
            
            
    def create_Ht_window(self):
        
        self.Ht=Ht()
        self.Ht.show()
        
    def create_St_window(self):
        
        self.setting=setting()
        self.setting.show()
        
    def create_Inicio_window(self):
        self.Inicio=Inicio()
        self.Inicio.show()
        
        
class Reminder(QMainWindow):        
    def __init__(self):
        super(Reminder, self).__init__()
        self.ui = Ui_Reminder()

        self.ui.setupUi(self)
        
        try:
            
            self.ui.B_Close.clicked.connect(self.close())
        except Exception as e:
            print(e)
class RechargeReminder(QMainWindow):        
    def __init__(self):
        super(RechargeReminder, self).__init__()
        self.ui = Ui_RechargeReminder()

        self.ui.setupUi(self)
        
        try:
            
            self.ui.B_Close.clicked.connect(self.close())
        except Exception as e:
            print(e)
class VideoCap(QMainWindow):        
    def __init__(self):
        super().__init__()
        
        # Controles principales para organizar la ventana.
        self.widget = QWidget(self)
        self.layout = QVBoxLayout()
        self.bottom_layout = QHBoxLayout()
        
        # Control de reproducción de video de Qt.
        self.video_widget = QVideoWidget(self)
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(VIDEO_PATH)))
        self.video_widget.resize(800,480)
        self.media_player.setVideoOutput(self.video_widget)
        # Personalizar la ventana.
        
        self.setWindowTitle("Reproductor de video")
        self.resize(800, 480)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
        # Reproducir el video.
        self.media_player.play()
        #print(self.media_player.EndOfMedia)
        self.media_player.setVolume(200)
        
                   
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
        lineEditPassword=self.ui.lineEditPassword.text()
        ftext=open(PinFile,'w')
        ftext.write(lineEditPassword)
        ftext.close()
        
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
                
    #def create_Inicio_window(self):
        #self.Inicio=Inicio()
        #self.Inicio.show()

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




