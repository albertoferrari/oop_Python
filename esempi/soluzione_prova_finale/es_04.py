'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Definire la classe Python Rettangolo che ha come attributi le misure 
della base e dell’altezza di un rettangolo e i metodi area() 
e perimetro(). Istanziare poi due rettangoli con misure a piacere 
e visualizzarne area e perimetro.
'''

class Rettangolo:
	'''
	rettangolo con misure di base e altezza
	'''
		
	def __init__(self, base: float, altezza: float):
		''' 
		inizializzazione attributi
		'''
		self._base = base
		self._altezza = altezza

	def perimetro(self) -> float:
		'''
		perimetro del rettangolo
		'''
		return (self._base + self._altezza) * 2
		
	def area(self) -> float:
		'''
		area del rettangolo
		'''
		return self._base * self._altezza
		
def main():
	r1 = Rettangolo(10,20)
	r2 = Rettangolo(12,4)
	print("perimetro del rettangolo r1",r1.perimetro())
	print("perimetro del rettangolo r2",r2.perimetro())	
	print("area del rettangolo r1",r1.area())	
	print("area del rettangolo r2",r2.area())	
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()
