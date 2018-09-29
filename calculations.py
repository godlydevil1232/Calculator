from stringparser import NumericStringParser

parser=NumericStringParser()
class Calculations:
	
	def __init__(self):

		self._calcString=""		
		self._result=0.0


	def update(self,value:str):

		self._calcString+=value


	def _arrange(self):

		self._result=parser.eval(self._calcString)

	def nullify(self):

		self._calcString=""


	def getResult(self):

		self._arrange()

		
		return self._result



