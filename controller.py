from PyQt5.QtWidgets import *
from view import Ui_MainWindow
import csv
import boston_mansheim
from PyQt5 import QtCore


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.circle_calculate_button.clicked.connect(lambda : self.circle())
        self.square_calculate_button.clicked.connect(lambda: self.square())
        self.triangle_calculate_button.clicked.connect(lambda: self.triangle())
        self.rectangle_calculate_button.clicked.connect(lambda: self.rectangle())

    def circle(self):
        _translate = QtCore.QCoreApplication.translate
        answer = boston_mansheim.circleArea(self.circle_entry.text())
        print(answer)
        self.circle_area_value.setText(_translate("MainWindow", f'{answer}'))

    def square(self):
        _translate = QtCore.QCoreApplication.translate
        answer = boston_mansheim.squareArea(self.square_entry.text())
        print(answer)
        self.square_area_value.setText(_translate("MainWindow", f'{answer}'))

    def triangle(self):
        _translate = QtCore.QCoreApplication.translate
        answer = boston_mansheim.triangleArea(self.triangle_length_entry.text(), self.triangle_width_entry.text())
        print(answer)
        self.triangle_area_value.setText(_translate("MainWindow", f'{answer}'))

    def rectangle(self):
        _translate = QtCore.QCoreApplication.translate
        answer = boston_mansheim.rectangleArea(self.rectangle_length_entry.text(), self.rectangle_width_entry.text())
        print(answer)
        self.rectangle_area_value.setText(_translate("MainWindow", f'{answer}'))
