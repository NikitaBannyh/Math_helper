from math import sqrt, factorial
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton


class Calculator(QWidget):  # класс калькулятора
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/calculator.ui', self)
        self.plus_ = []
        self.minus_ = []
        self.division_ = []
        self.umn_ = []
        self.degree_ = []
        self.x = '0'
        self.lcdNumber.display(self.x)
        self.one.clicked.connect(self.nums)
        self.two.clicked.connect(self.nums)
        self.three.clicked.connect(self.nums)
        self.four.clicked.connect(self.nums)
        self.five.clicked.connect(self.nums)
        self.six.clicked.connect(self.nums)
        self.seven.clicked.connect(self.nums)
        self.eight.clicked.connect(self.nums)
        self.nine.clicked.connect(self.nums)
        self.zero.clicked.connect(self.nums)
        self.plus.clicked.connect(self._plus)
        self.equal.clicked.connect(self._equal)
        self.minus.clicked.connect(self._minus)
        self.division.clicked.connect(self._division)
        self.umn.clicked.connect(self._umn)
        self.ac.clicked.connect(self._ac)
        self.degree.clicked.connect(self._degree)
        self.fact.clicked.connect(self._fact)
        self.sqrt.clicked.connect(self._sqrt)
        self.point.clicked.connect(self._point)
        self.show()

    def nums(self):  # функция кнопок калькулятора отвечающие за числа
        button = self.sender()
        if self.x == '0':
            self.x = button.text()
            self.lcdNumber.display(self.x)
        else:
            self.x += button.text()
            if len(self.x) <= 9:
                self.lcdNumber.display(self.x)
            else:
                pass

    def _point(self):  # функция добавляющая точку
        if '.' not in self.x:
            self.x += '.'
            self.lcdNumber.display(self.x)
        else:
            pass

    def _equal(self):  # функция равно
        if len(self.plus_) != 0:
            if '.' in self.x:
                self.plus_.append(float(self.x))
            else:
                self.plus_.append(int(self.x))
            self.x = str(sum(self.plus_))
            if len(str(self.x)) >= 9:
                QMessageBox.about(self, 'Ошибка', ' Слишком большое число \n Ответ: ' + str(self.x))
                self.x = '0'
                self.lcdNumber.display(self.x)
            else:
                self.lcdNumber.display(self.x)
            self.plus_.clear()
        if len(self.minus_) != 0:
            if '.' in self.x:
                self.minus_.append(float(self.x))
            else:
                self.minus_.append(int(self.x))
            self.x = str(self.minus_[0] - self.minus_[1])
            if len(str(self.x)) >= 9:
                QMessageBox.about(self, 'Ошибка', ' Слишком большое число \n Ответ: ' + str(self.x))
                self.x = '0'
                self.lcdNumber.display(self.x)
            else:
                self.lcdNumber.display(self.x)
            self.minus_.clear()
        if len(self.division_) != 0:
            if '.' in self.x:
                self.division_.append(float(self.x))
            else:
                self.division_.append(int(self.x))
            if self.division_[1] != 0:
                self.x = self.division_[0] / self.division_[1]
                self.lcdNumber.display(str(self.x)[:10])
                self.division_.clear()
            else:
                QMessageBox.about(self, 'Ошибка', 'Делить на 0 нельзя!')
                self.x = '0'
                self.lcdNumber.display(int(self.x))
                self.division_.clear()
        if len(self.umn_) != 0:
            if '.' in self.x:
                self.umn_.append(float(self.x))
            else:
                self.umn_.append(int(self.x))
            self.x = str(self.umn_[0] * self.umn_[1])
            if len(str(self.x)) >= 9:
                QMessageBox.about(self, 'Ошибка', ' Слишком большое число \n Ответ: ' + str(self.x))
                self.x = '0'
                self.lcdNumber.display(self.x)
            else:
                self.lcdNumber.display(self.x)
            self.umn_.clear()
        if len(self.degree_) != 0:
            if '.' in self.x:
                self.degree_.append(float(self.x))
            else:
                self.degree_.append(int(self.x))
            self.x = str(self.degree_[0] ** self.degree_[1])
            if len(str(self.x)) >= 9:
                QMessageBox.about(self, 'Ошибка', ' Слишком большое число \n Ответ: ' + str(self.x))
                self.x = '0'
                self.lcdNumber.display(self.x)
            else:
                self.lcdNumber.display(self.x)
            self.degree_.clear()

    def _plus(self):  # функция плюса
        if '.' in str(self.x):
            self.plus_.append(float(self.x))
        else:
            self.plus_.append(int(self.x))
        self.x = '0'
        self.lcdNumber.display(int(self.x))

    def _minus(self):  # функция минуса
        if '.' in str(self.x):
            self.minus_.append(float(self.x))
        else:
            self.minus_.append(int(self.x))
        self.x = '0'
        self.lcdNumber.display(int(self.x))

    def _division(self):  # функция деления
        if '.' in str(self.x):
            self.division_.append(float(self.x))
        else:
            self.division_.append(int(self.x))
        self.x = '0'
        self.lcdNumber.display(int(self.x))

    def _umn(self):  # функция умножения
        if '.' in str(self.x):
            self.umn_.append(float(self.x))
        else:
            self.umn_.append(int(self.x))
        self.x = '0'
        self.lcdNumber.display(int(self.x))

    def _ac(self):  # функция очистки
        self.x = '0'
        self.lcdNumber.display(int(self.x))
        self.plus_.clear()
        self.minus_.clear()
        self.division_.clear()
        self.umn_.clear()
        self.degree_.clear()

    def _degree(self):  # функция степени
        if '.' in str(self.x):
            self.degree_.append(float(self.x))
        else:
            self.degree_.append(int(self.x))
        self.x = '0'
        self.lcdNumber.display(int(self.x))

    def _fact(self):  # функция факториала
        self.x = str(factorial(int(self.x)))
        if len(str(self.x)) >= 9:
            QMessageBox.about(self, 'Ошибка', ' Слишком большое число \n Ответ: ' + str(self.x))
            self.x = '0'
            self.lcdNumber.display(self.x)
        else:
            self.lcdNumber.display(self.x)

    def _sqrt(self):  # функция корня
        if int(self.x) >= 0:
            self.x = str(sqrt(int(self.x)))
            self.lcdNumber.display(str(self.x)[:10])
        else:
            QMessageBox.about(self, 'Ошибка', 'Нельзя вычислить степень из отрицательного числа!')
            self.x = '0'
            self.lcdNumber.display(self.x)
