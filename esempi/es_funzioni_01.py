'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Scrivere la funzione volume che riceve come parametri le misure degli spigoli
di un parallelepipedo rettangolo e restituisce il volume. Scrivere un
programma che richiede in input le misure di un parallelepipedo rettangolo e,
utilizzando la funzione volume stampa il volume.
'''

def volume(x: float, y: float, z: float) -> float:
	'''
	x,y,z spigoli parallelepipedo rettangolo
	restituisce volume parallelepipedo
	'''
	vol = x * y * z
	return vol 
	
def main():
	l = float(input("larghezza : "))
	h = float(input("altezza   : "))
	p = float(input("profondità: "))	
	print("volume",volume(l,h,p))

main()

