'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Scrivere la funzione isPrimo che restituisce True se il parametro ricevuto è un
numero primo. Visualizzare tutti i numeri primi compresi fra 1 e 100.
'''

def isPrimo(n: int) -> bool:
	'''
	True se n è primo
	'''
	for d in range(2,n):		#d possibile divisore tra 2 e n-1
		if (n % d) == 0:		#ho trovato un divisore
			return False		#n non è primo
	return True
	
def main():
	for i in range(1,101):
		if isPrimo(i):			#i è un numero primo
			print(i)

main()

