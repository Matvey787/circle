import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Фокус со словами')
        self.button = QPushButton(self)
        self.button.setGeometry(100, 100, 100, 100)
        self.colors = ['Red', 'Orange', 'Yellow', 'Green',
                       'Blue', 'Purple', 'Brown', 'Black']

        self.button.clicked.connect(self.drawing)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(self,qp):
        self.do_paint = True
        qp.setBrush(QColor(choice(self.colors)))
        a = randint(1, 100)
        qp.drawEllipse(0, 0, a, a)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())