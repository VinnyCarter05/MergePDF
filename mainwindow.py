from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow_ui import Ui_MainWindow
import logging, os
from PyPDF2 import PdfFileMerger

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    #Signals
    dropFile_signal = QtCore.pyqtSignal(str)
    delete_list_item_signal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        

        # variables
        self.PDF_list = []
        self.PDF_count = 0 # number of PDFs
        self.save_filename = ''

        self.setupUi(self)
        self.show()

        # setting drag drop mode
        self.listWidget_PDF.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        # self.listWidget_PDF.setSortingEnabled(True)

        # getting PDFlist
        self.get_PDF_list_and_PDF_count()

        # connect to slots
        self.dropFile_signal.connect(self.add_drop_to_list)
        self.delete_list_item_signal.connect(self.delete_list_item)
        self.actionAdd_PDF.triggered.connect(self.open_files)
        self.actionMerge_and_Save_PDF.triggered.connect(self.save_file)
        self.actionQuit.triggered.connect(self.exit)

    def get_PDF_list_and_PDF_count(self):
        self.PDF_count = self.listWidget_PDF.count()
        self.PDF_list = []
        logging.debug(f'PDF_count = {self.PDF_count}')
        for item in range(self.PDF_count):
            self.PDF_list.append (self.listWidget_PDF.item(item).text())
            logging.debug(f'list widget PDF {item} = {self.PDF_list[item]}')

    def dragEnterEvent(self,e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.dropFile_signal.emit(e.mimeData().text())

    def add_drop_to_list(self, filename):
        try:
            _, filename = filename.split('///') #network path
        except:
            try:
                _, filename = filename.split(':')
            except:
                return
        if os.path.isfile(filename) and filename.lower().endswith(".pdf"):
            self.addFormattedItem(filename)

    def addFormattedItem(self, filename):
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/up-and-down.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        item.setIcon(icon)
        item.setText(filename)
        self.listWidget_PDF.addItem(item)

    def delete_list_item (self):
        self.listWidget_PDF.takeItem(self.listWidget_PDF.currentRow())

    def open_files (self):
        options = QtWidgets.QFileDialog.Options()
        fileNames, _ = QtWidgets.QFileDialog.getOpenFileNames(self
            ,"Files to Merge", "","PDF files (*.pdf);; All Files (*)", options=options)
        for filename in fileNames:
            if (os.path.splitext(filename)[1].lower()) == ".pdf":
                self.addFormattedItem(filename)

    def save_file (self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self
            ,"Save to", "","PDF files (*.pdf);; All Files (*)", options=options)
        if fileName:
            self.save_filename = fileName
            logging.debug(f"save file: {self.save_filename}")
            self.merge_PDF()

    def merge_PDF(self):
        merger = PdfFileMerger()
        self.get_PDF_list_and_PDF_count()

        for pdf in self.PDF_list:
            merger.append(pdf)

        merger.write(f"{self.save_filename}")
        merger.close

    def exit(self):
            logging.debug("Escape:  ")
            self.get_PDF_list_and_PDF_count()
            self.close()



    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.exit()
        if e.key() == QtCore.Qt.Key_Delete:
            self.delete_list_item_signal.emit()
        if e.key() == QtCore.Qt.Key_Insert:
            self.open_files()
        if e.key() == QtCore.Qt.Key_F1:
            self.save_file()


