import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow
from Ht import Ui_MainWindow


class Ht(QMainWindow):
    def __init__(self):
        super(Ht, self).__init__()
        try:

            self.ui = Ui_MainWindow()

            self.ui.setupUi(self)
        except Exception as e:
                print(e)


#hola soy ana
app = QApplication([])

application = Ht()

application.show()

sys.exit(app.exec())

GPIO.cleanup()
