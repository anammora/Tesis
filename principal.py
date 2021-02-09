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
            self.ui.dateTimeC1.dateTimeChanged.connect(self.Change2)
        except Exception as e:
                print(e)

    def Change2(self,CurrentDT):
        self.ui.dateTimeC2.setMinimumDateTime(CurrentDT)
#hola soy ana
app = QApplication([])

application = Ht()

application.show()

sys.exit(app.exec())

GPIO.cleanup()
