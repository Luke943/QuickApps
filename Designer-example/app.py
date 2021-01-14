'''
File to run the app
Creates class that innherits layout of UI from containerUI and adds functionality
Executes if run as __main__
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from containerUI import Ui_MainWindow


class App_MainWindow(Ui_MainWindow):

    def setup_app(self, MainWindow):
        # inherit layout from Ui_MainWindow
        self.setupUi(MainWindow)

        # connect widgets to methods
        self.selectImageBtn.clicked.connect(self.set_image)
        self.addBtn.clicked.connect(self.add_item)

    def set_image(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select image", "", "Image files (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            pixmap = QtGui.QPixmap(filename)
            pixmap = pixmap.scaled(self.imageLbl.width(
            ), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)

    def add_item(self):
        value = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.addItem(value)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App_MainWindow()
    ui.setup_app(MainWindow)
    app.setStyle('fusion')
    MainWindow.show()
    sys.exit(app.exec_())
