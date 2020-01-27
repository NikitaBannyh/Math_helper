import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator import Calculator
from quadratic_equation import Quadratic_equation
from graphs import Graph


class Main(QMainWindow):  # класс главного меню
    def __init__(self):
        super().__init__()

        uic.loadUi('ui_files/mainwindow.ui', self)
        self.calcul.clicked.connect(self.cal)
        self.quatro.clicked.connect(self.quad)
        self.graph.clicked.connect(self.graph_)

    def cal(self):  # три функции открывающие новые виджеты
        self.widget = Calculator()

    def quad(self):
        self.widget_1 = Quadratic_equation()

    def graph_(self):
        self.widget_3 = Graph()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
