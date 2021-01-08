from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys
import logging

from mainwindow import MainWindow

# set taskbar icon
import ctypes
myappid = u'MFMC.MFMC-MergePDF.PDF.10' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



if __name__ == '__main__':
    logging.basicConfig(filename='MergePDF.log', encoding='utf-8', level=logging.ERROR)

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
       
 
    sys.exit(app.exec_())