'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Dalla classe Rettangolo dell’esercizio precedente definire la classe 
derivata RettangoloColorato che ha l’attributo colore (tripla R,G,B) 
e il metodo schiarisci(p) che diminuisce ogni componente colore 
del p per cento 
'''

from es_04 import Rettangolo

class RettangoloColorato(Rettangolo):
	'''
	rettangolo con misure di base e altezza
	'''
		
	def __init__(self, base: float, altezza: float, colore: [int,int,int]):
		''' 
		inizializzazione attributi
		'''
		self._base = base
		self._altezza = altezza
		self._colore = colore

	def getColore(self) -> (int,int,int):
		'''
		colore del rettangolo
		'''
		return self._colore
	
	def schiarisci(self, p) -> None:
		'''
		diminuisce ogni componente colore di p%
		'''
		self._colore[0] = int(self._colore[0]*(100-p)/100)
		self._colore[1] = int(self._colore[1]*(100-p)/100)
		self._colore[2] = int(self._colore[2]*(100-p)/100)
		
		
def main():
	rc = RettangoloColorato(10,20,[255,255,100])
	print("perimetro del rettangolo rc",rc.perimetro())
	print("area del rettangolo rc",rc.area())	
	print(rc.getColore())
	for i in range(5):
		rc.schiarisci(10)
		print(rc.getColore())	
		
	
main()
