'''
Creates instance of MainWindow class for calculator
Styled by creating instance of QtGui.QPalette
'''

import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore, QtGui, QtWidgets

from calculator import MainWindow

app = qtw.QApplication([])

# apply styling https://gist.github.com/gph03n1x/7281135
app.setStyle('Fusion')
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

palette.setColor(QtGui.QPalette.Highlight,
                 QtGui.QColor(142, 45, 197).lighter())
palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
app.setPalette(palette)
font = QtGui.QFont()
font.setPointSize(20)
app.setFont(font)

main_window = MainWindow()
app.exec_()
