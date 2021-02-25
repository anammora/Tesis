import sys,os
from PyQt5.QtWidgets import (QWidget,QApplication,QPushButton,
                             QVBoxLayout,QFileDialog,QHBoxLayout)
#from pygame import mixer                                         # ---
import pygame                                                     # +++
pygame.init()                                                     # +++

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.playsound = None                                     # +++
        self.pause     = None                                     # +++

        self.init_ui()

    def init_ui(self):
        self.song1 = QPushButton("LoadingSound")
        self.pause = QPushButton("Pause")
        self.play_it = QPushButton("Play")
        h_box = QHBoxLayout()
        h_box.addWidget(self.song1)
        h_box.addWidget(self.play_it)
        h_box.addWidget(self.pause)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("Song Mixer 1.0")

        self.song1.clicked.connect(self.song1_open)
        self.pause.clicked.connect(self.pause_the_songs)            
        self.play_it.clicked.connect(self.play_the_songs)

        self.show()

    def pause_the_songs(self):
        if self.playsound is None:
            self.pause.setText("UnPause")
            self.playsound = "pause"
            pygame.mixer.music.pause()
        else:
            self.pause.setText("Pause")
            self.playsound = None  
            pygame.mixer.music.unpause()            

    def song1_open(self):
        file_name = QFileDialog.getOpenFileName(self,"Open",os.getenv("HOME"))
        self.data1 = file_name[0]

    def play_the_songs(self):                                     # +++
        self.playsound = pygame.mixer.init()        
        pygame.mixer.music.load(self.data1)
        pygame.mixer.music.play()


app = QApplication(sys.argv)
pencere = Window()
sys.exit(app.exec_())