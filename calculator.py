from graphics import Graphics
from calculations import Calculations
from PyQt4 import QtGui
from PyQt4 import QtCore

gui=Graphics()
calc=Calculations()
class Calculator():

	
	def createWindow(self):

		
		self._window=gui.newWidget("Calculator")


	def createDisplay(self):

		self._lcd=gui.createLCD()
		self.setDisplayStyle(self._lcd)

	def createProgression(self):

		self._label=gui.addLabel("")
		self._label.setFixedHeight(10)
		self._label.setFont(QtGui.QFont("Gill Sans MT",10))


	def createLayouts(self):

		self._box=gui.createBoxLayout()
		self._grid=gui.createGridLayout()


	def defineWindow(self):

		self._box.addWidget(self._label)
		self._box.addWidget(self._lcd)
		

		self._positions=[(i,j)for i in range(5) for j in range(4)]
		
		for (position,name) in zip(self._positions,self._names):
			button=gui.addButton(name)
			gui.onClick(button,lambda :self.buttonClicked(button))
			self._grid.addWidget(button,*position)
			self.setButtonStyle(button)

		self._box.addLayout(self._grid)
		self._window.setLayout(self._box)
		self._window.resize(400,400)

		self._window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
		gui.getApp().setWindowIcon(QtGui.QIcon("icon.ico"))


		


	def buttonClicked(self,button):

		bt=button.sender().text()
		if (bt=="="):
			self._label.setText(f"{calc._calcString}={calc.getResult()}")
			self._lcd.display(calc.getResult())
		else:
			if bt in["+","-","*","/"]:
				calc.update(bt)	
				self._label.setText(calc._calcString)			
				self._buffer=""
			elif bt=="CE":
				self._buffer=""
				self._label.setText(calc._calcString)
				calc.nullify()
				self._lcd.display("")
			else:
				self._buffer+=bt
				calc.update(bt)
				self._lcd.display(self._buffer)
				self._label.setText(calc._calcString)



	def setButtonStyle(self,button):

		button.setStyleSheet("QPushButton { background-color: #D3D3D3 ;color:black;border-radius:50%,padding:50px;border:none}"
                      "QPushButton:pressed { background-color: red }" )

		button.setFixedHeight(45)

	def setDisplayStyle(self,LCD):

		LCD.setStyleSheet("QLCDNumber{color:black")


	def __init__(self):
		
		self._buffer=""
		self._names=['CE','7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
		self.createWindow()
		self.createProgression()
		self.createDisplay()
		self.createLayouts()
		self.defineWindow()
		gui.start()

if __name__ == '__main__':
	Calculator()

