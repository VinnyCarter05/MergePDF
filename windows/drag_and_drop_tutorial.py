# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 

class MainWindow(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		# setting title 
		self.setWindowTitle("Python ") 

		# setting geometry 
		self.setGeometry(100, 100, 500, 400) 

		# calling method 
		self.UiComponents() 

		# showing all the widgets 
		self.show() 



	# method for components 
	def UiComponents(self): 

		# creating a QListWidget 
		list_widget = QListWidget(self) 

		# setting geometry to it 
		list_widget.setGeometry(50, 70, 150, 60) 

		# list widget items 
		item1 = QListWidgetItem("A") 
		item2 = QListWidgetItem("B") 
		item3 = QListWidgetItem("C") 

		# adding items to the list widget 
		list_widget.addItem(item1) 
		list_widget.addItem(item2) 
		list_widget.addItem(item3) 

		# setting drag drop mode 
		list_widget.setDragDropMode(QAbstractItemView.DragDrop) 

		# creating a label 
		label = QLabel("GeesforGeeks", self) 

		# setting geometry to the label 
		label.setGeometry(230, 80, 280, 80) 

		# making label multi line 
		label.setWordWrap(True) 

