'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
In matematica due numeri primi si dicono sexy quando la loro differenza è
uguale a sei. Il nome di queste coppie di numeri primi deriva dalla parola latina
sex (ovvero sei). Es. (11,17) è una coppia di primi sexy come pure (67, 73).
Scrivere un programma che visualizza tutte le coppie di primi sexy con
valori compresi fra 1 e 100
'''

def isPrimo(n: int) -> bool:
	'''
	True se n è primo
	'''
	for d in range(2,n):
		if n % d == 0:
			return False	
	return True
	
def main():
	for i in range(1,95):
		if isPrimo(i) and isPrimo(i+6):
			print(i,i+6)	

main()

