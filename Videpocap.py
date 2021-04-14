'''
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QDate, QTime, QObject,QDateTime, Qt, QThread, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow
from PyQt5.QtGui import QImage

def run(self):
    cap = cv2.VideoCapture('/media/pi/MORAMO/VIDEO(1)/abuela con Alzheimer reconoce.mp4')

    while(cap.isOpened()):
       print('hello') 
       ret, frame = cap.read()
       rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
       convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
       p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
       self.changePixmap.emit(p)
       if ret==False:
           break
       frame=cv2.resize(frame,(800,480))
       
       #cv2.imshow('VIDEO',frame)
       
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    cap.release()   
    cv2.destroyAllWindows()


# importing vlc module
#import vlc
 
# creating vlc media player object
#media = vlc.MediaPlayer("/media/pi/MORAMO/VIDEO(1)/abuela con Alzheimer reconoce.mp4")
 
# start playing video
#media.play()
'''

# importing vlc module
import vlc
import time 
  
# creating vlc media player object
media_player = vlc.MediaPlayer()
  
# media object
media = vlc.Media("/media/pi/MORAMO/VIDEO(1)/abuela con Alzheimer reconoce.mp4")
  
# setting media to the media player
media_player.set_media(media)
  
# setting video scale
media_player.video_set_scale(0.55)
  
# start playing video
media_player.play()
