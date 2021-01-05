from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys
import logging

from windows.mainwindow import MainWindow



if __name__ == '__main__':
    logging.basicConfig(filename='MergePDF.log', encoding='utf-8', level=logging.DEBUG)

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
       
 
    sys.exit(app.exec_())