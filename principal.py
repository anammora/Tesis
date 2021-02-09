from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication, QMainWindow
from Ht import Ui_MainWindow







app = QApplication([])

application = Ht()

##application.show()

sys.exit(app.exec())

GPIO.cleanup()
