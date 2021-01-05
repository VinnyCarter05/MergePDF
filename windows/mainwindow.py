from PyQt5 import QtCore, QtGui, QtWidgets
from windows.mainwindow_ui import Ui_MainWindow
import logging

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # variables
        self.PDF_list = []
        self.PDF_count = 0 # number of PDFs

        self.setupUi(self)
        self.show()

        # setting drag drop mode
        self.listWidget_PDF.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget_PDF.setSortingEnabled(True)

        # getting PDFlist
        self.get_PDF_list_and_PDF_count()

    def get_PDF_list_and_PDF_count(self):
        self.PDF_count = self.listWidget_PDF.count()
        self.PDF_list = []
        logging.debug(f'PDF_count = {self.PDF_count}')
        for item in range(self.PDF_count):
            self.PDF_list.append (self.listWidget_PDF.item(item).text())
            logging.debug(f'list widget PDF {item} = {self.PDF_list[item]}')

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


