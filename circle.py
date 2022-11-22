from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class Focus(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.x = -1
        self.y = -1
        self.k = 0
        self.button = QPushButton(self)
        self.button.setGeometry(100, 100, 100, 100)
        self.colors = ['Red', 'Orange', 'Yellow', 'Green',
                       'Blue', 'Purple', 'Brown', 'Black']
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('-----------------------------------------------------------------------------------------')
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawing(self, qp):
        qp.setBrush(QColor('Yellow'))
        a = randint(1, 1000)
        qp.drawEllipse(300, 300, a, a)



if __name__ == '__main__':
    app = QApplication(argv)
    ex = Focus()
    ex.show()
    exit(app.exec())