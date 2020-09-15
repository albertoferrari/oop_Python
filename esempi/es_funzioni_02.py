'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Scrivere le funzione isTriangoloRettangolo che riceve come parametri 3
valori e restituisce True se questi possono essere i lati di un triangolo
rettangolo. Utilizzando la funzione richiedere in input 3 valori e verificare se
possono essere i lati di un triangolo rettangolo
'''

def isTriangoloRettangolo(a: float, b: float, c: float) -> bool:
	'''
	verifica se a b c sono le misure di un triangolo rettangolo
	'''
	if a<=0 or b<=0 or c<=0:			#almeno un lato negativo
		return False
	if a>=b+c or b>=a+c or c>=a+b:		#errore misura lati
		return False
	if a**2 == b**2 + c**2:				# a è ipotenusa
		return True
	if b**2 == a**2 + c**2:				# b è ipotenusa
		return True	
	if c**2 == b**2 + a**2:				# c è ipotenusa
		return True		
	return False						#è un triangolo ma non rettangolo
	
def main():
	l1 = float(input("lato 1: "))
	l2 = float(input("lato 2: "))
	l3 = float(input("lato 3: "))	
	if isTriangoloRettangolo(l1,l2,l3):
		print("sono i lati di un triangolo rettangolo")
	else:
		print("non sono i lati di un triangolo rettangolo")		

main()

