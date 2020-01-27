from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Graph(QWidget):  # класс построения графиков
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/graph.ui', self)
        self.kind.addItem('y = kx')
        self.kind.addItem('y = kx + b')
        self.kind.addItem('y = x^2')
        self.kind.addItem('y = -x^2')
        self.kind.addItem('y = x^3')
        self.kind.addItem('y = -x^3')
        self.btn.clicked.connect(self.graphics_)
        self.show()

    def graphics_(self):  # всего одна функция которая стрит сами графики
        self.k = self.var_k.text()
        self.b = self.var_b.text()
        if self.kind.currentText() == 'y = kx' and self.k != '':
            self.graphics.clear()
            self.graphics.plot([i for i in range(-10, 10)], [i * int(self.k) for i in range(-10, 10)], pen='r')
            self.var_k.clear()
            self.var_b.clear()
            self.name.setText('y = ' + self.k + 'x:')
        elif self.kind.currentText() == 'y = kx + b' and self.k != '' and self.b != '':
            self.graphics.clear()
            self.graphics.plot([i for i in range(-10, 10)], [(i * int(self.k)) + int(self.b) for i in range(-10, 10)],
                               pen='r')
            self.var_k.clear()
            self.var_b.clear()
            self.name.setText('y = ' + self.k + 'x + ' + self.b + ':')
        elif self.kind.currentText() == 'y = x^2':
            self.graphics.clear()
            self.graphics.plot([i for i in range(-10, 10)], [i ** 2 for i in range(-10, 10)], pen='r')
            self.var_k.clear()
            self.var_b.clear()
            self.name.setText('y = x^2:')
        elif self.kind.currentText() == 'y = -x^2':
            self.graphics.clear()
            self.graphics.plot([i for i in range(-10, 10)], [-i ** 2 for i in range(-10, 10)], pen='r')
            self.var_k.clear()
            self.var_b.clear()
            self.name.setText('y = -x^2:')
        elif self.kind.currentText() == 'y = x^3':
            self.graphics.clear()
            self.graphics.plot([i for i in range(-10, 10)], [i ** 3 for i in range(-10, 10)], pen='r')
            self.var_k.clear()
            self.var_b.clear()
            self.name.setText('y = x^3:')
        elif self.kind.currentText() == 'y = -x^3':
            self.graphics.clear()
            self.graphics.plot([i for i in range(-10, 10)], [-i ** 3 for i in range(-10, 10)], pen='r')
            self.var_k.clear()
            self.var_b.clear()
            self.name.setText('y = -x^3:')
