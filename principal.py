from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication, QMainWindow
from Ht import Ui_MainWindow






#hola soy ana 
app = QApplication([])

application = Ht()

##application.show()

sys.exit(app.exec())

GPIO.cleanup()
