from math import sqrt
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QWidget


class Quadratic_equation(QWidget):  # класс квадратных уравнений
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/quadro.ui', self)
        self.btn.clicked.connect(self.decision)
        self.ok.clicked.connect(self.ok_)
        self.show()

    def decision(self):  # функция нахождения дискриминанта и корней
        a = float(self.a_.text())
        b = float(self.b_.text())
        c = float(self.c_.text())
        if a == 0:
            QMessageBox.about(self, 'Ошибка', 'Коэффициент а не может быть равен 0')
            self.a_.clear()
        else:
            discr = b ** 2 - 4 * a * c
            self.dicscriminant.setText(str(int(discr)))
            if discr > 0:
                x1 = (-b + sqrt(discr)) / (2 * a)
                x2 = (-b - sqrt(discr)) / (2 * a)
                self.x1.setText('x1 = ' + str(x1)[:7])
                self.x2.setText('x2 = ' + str(x2)[:7])
            elif discr == 0:
                self.dicscriminant.setText(
                    str(int(discr)))
                self.d_.setText('D = 0, следовательно \nуравнение имеет \nодин действительный корень.')
                x = -b / (2 * a)
                self.x1.setText('x =' + str(x))
            else:
                self.d_.setText('D < 0, следовательно \nуравнение не имеет \nдействительных корней.')

    def ok_(self):  # функция очистки
        self.a_.clear()
        self.b_.clear()
        self.c_.clear()
        self.x1.clear()
        self.x2.clear()
        self.d_.clear()
        self.dicscriminant.clear()
