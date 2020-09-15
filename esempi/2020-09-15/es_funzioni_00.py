'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di funzioni (area ellisse)
'''
import math

def areaEllisse(a: float, b: float) -> float:
	'''
	dati a e b semiassi 
	restituisce area ellisse
	'''
	area = math.pi * a * b
	return area 
	
def main():
	s1 = float(input("lunghezza primo   semiasse: "))
	s2 = float(input("lunghezza secondo semiasse: "))	
	area = areaEllisse(s1,s2)
	print("Area dell'ellisse",area)
	
main()

