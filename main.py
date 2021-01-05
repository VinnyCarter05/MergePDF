from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys

from windows.mainwindow import MainWindow

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
       
 
    sys.exit(app.exec_())