'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Palla (si muove nel canvas)
'''

class Palla:
	'''
	rappresenta un oggetto che si muove 
	in uno spazio bidimensionale
	'''
		
	def __init__(self, x: int, y: int, dx: int = 5, dy: int  = 5):
		''' 
		inizializzazione attributi
		'''
		self._x = x
		self._y = y
		self._dx = dx
		self._dy = dy
		self._w = 20
		self._h = 20

	def muovi(self):
		'''
		sposta la pallina secondo le direzioni dx e dy
		'''
		if not (0 <= self._x + self._dx <= ARENA_L - self._w):
			self._dx = -self._dx
		if not (0 <= self._y + self._dy <= ARENA_H - self._h):
			self._dy = -self._dy
		self._x += self._dx
		self._y += self._dy

	def posizione(self) -> (int, int, int, int):
		'''
		restituisce coordinate e dimensioni della pallina
		'''
		return self._x, self._y, self._w, self._h


ARENA_L = 320			# larghezza arena
ARENA_H = 240			# altezza arena

def main():
	p1 = Palla(10,20)
	p2 = Palla(34,40,12,23)
	for i in range(1,80):
		print('p1 si trova in posizione',p1.posizione())
		print('p2 si trova in posizione',p2.posizione())
		p1.muovi()
		p2.muovi()
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()



