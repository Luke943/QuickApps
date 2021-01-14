'''
This file contains the MainWindow class for the calculator used in the app
'''

import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

operations = {'+': '+', '-': '-', 'x': '*', '÷': '/'}


class MainWindow(qtw.QWidget):
    '''
    Create a class that inherits from QWidget class (empty screen)
    '''

    def __init__(self):
        # main window
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())  # create box layout
        self.keypad()
        self.display = '0'
        self.memory_string = ''
        self.last_press = 'equal'

        self.result_field.setText(self.display)
        self.show()

    def keypad(self):
        # empty container for buttons
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # buttons
        self.result_field = qtw.QLineEdit()
        self.result_field.setReadOnly(True)
        self.result_field.setAlignment(qtc.Qt.AlignRight)   
        btn_result = qtw.QPushButton('Enter', clicked=self.func_result)
        btn_clear = qtw.QPushButton('Clear', clicked=self.clear_calc)
        btn_9 = qtw.QPushButton('9', clicked=lambda: self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked=lambda: self.num_press('0'))
        btn_dot = qtw.QPushButton('.', clicked=lambda: self.num_press('.'))
        btn_plus = qtw.QPushButton('+', clicked=lambda: self.func_press('+'))
        btn_minus = qtw.QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_mult = qtw.QPushButton('x', clicked=lambda: self.func_press('x'))
        btn_div = qtw.QPushButton('÷', clicked=lambda: self.func_press('÷'))

        # add to layout
        container.layout().addWidget(self.result_field, 0, 0, 1, 5)
        container.layout().addWidget(btn_7, 1, 0)
        container.layout().addWidget(btn_8, 1, 1)
        container.layout().addWidget(btn_9, 1, 2)
        container.layout().addWidget(btn_clear, 1, 3, 1, 2)
        container.layout().addWidget(btn_4, 2, 0)
        container.layout().addWidget(btn_5, 2, 1)
        container.layout().addWidget(btn_6, 2, 2)
        container.layout().addWidget(btn_mult, 2, 3)
        container.layout().addWidget(btn_div, 2, 4)
        container.layout().addWidget(btn_1, 3, 0)
        container.layout().addWidget(btn_2, 3, 1)
        container.layout().addWidget(btn_3, 3, 2)
        container.layout().addWidget(btn_plus, 3, 3)
        container.layout().addWidget(btn_minus, 3, 4)
        container.layout().addWidget(btn_0, 4, 0, 1, 2)
        container.layout().addWidget(btn_dot, 4, 2)
        container.layout().addWidget(btn_result, 4, 3, 1, 2)
        self.layout().addWidget(container)

    def num_press(self, key_number):
        if self.last_press == 'num':
            self.display += key_number
            self.memory_string += key_number
        elif self.last_press == 'op':
            self.display = key_number
            self.memory_string += key_number
        elif self.last_press == 'equal':
            self.display = key_number
            self.memory_string = key_number
        self.last_press = 'num'
        self.result_field.setText(self.display)

    def func_press(self, operation):
        if self.last_press == 'num':
            evaluated = str(eval(self.memory_string))
            self.memory_string = evaluated + operations[operation]
            self.display = evaluated + operation
            self.last_press = 'op'           
        elif self.last_press == 'op':
            self.memory_string = self.memory_string[:-1] + operations[operation]
            self.display = self.display[:-1] + operation
        elif self.last_press == 'equal':
            self.memory_string = self.display
            self.display += operation
            self.memory_string += operations[operation]
        self.result_field.setText(self.display)

    def func_result(self):
        self.memory_string = str(eval(self.memory_string))
        self.display = self.memory_string
        self.last_press = 'equal'
        self.result_field.setText(self.display)

    def clear_calc(self):
        self.display = '0'
        self.memory_string = ''
        self.last_press = 'equal'
        self.result_field.setText(self.display)
