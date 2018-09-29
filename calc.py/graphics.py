import sys
from PyQt4 import QtGui

class Graphics:
	def __init__(self):

		self.app=QtGui.QApplication(sys.argv)
		self.widgets=[]
		self.labels=[]
		self.buttons=[]

	
	def createApp(self):
		return QtGui.QApplication(sys.argv)


	def getApp(self):

		return self.app


	def newWidget(self,name:str):

		w=QtGui.QWidget()
		self.widgets.append(w)
		return w	


	def addButton(self,text:str):

		b=QtGui.QPushButton(text)
		self.buttons.append(b)
		return b


	def addLabel(self,text:str):

		l=QtGui.QLabel()
		l.setText(text)
		self.labels.append(l)
		return l


	def onClick(self,btn:QtGui.QPushButton,func):
		return btn.clicked.connect(func)


	def createBoxLayout(self):
		return QtGui.QVBoxLayout()


	def createGridLayout(self):
		return QtGui.QGridLayout()


	def createLCD(self):
		return QtGui.QLCDNumber()

	def start(self):
		[widget.show() for widget in self.widgets]
		sys.exit(self.app.exec_())


