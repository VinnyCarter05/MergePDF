from PyQt5 import QtCore, QtGui, QtWidgets
from windows.mainwindow_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.show()

        # setting drag drop mode
        self.listWidget_PDF.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)