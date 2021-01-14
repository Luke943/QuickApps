'''
Creates instance of MainWindow class for calculator
Styled by importing a .qss file
'''

import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore, QtGui, QtWidgets
from calculator import MainWindow

# location of style sheet
sshFile = "darkbreeze.qss"

app = qtw.QApplication([])

# import style sheet
with open(sshFile, 'r') as fh:
    app.setStyleSheet(fh.read())

# increase font size so you don't need a microscope
font = QtGui.QFont()
font.setPointSize(18)
app.setFont(font)

main_window = MainWindow()
app.exec_()
