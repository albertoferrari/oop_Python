'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Scrivere un programma che richiede in input un numero intero
positivo (se il numero non è positivo richiederlo nuovamente) e
visualizza tutti i suoi divisori.
'''

n = int(input("valore intero positivo "))
# richiesta nuovo input se errato
while n <= 0:
	print("il numero deve essere positivo")
	n = int(input("valore intero positivo "))

div = 2 	# possibile divisore

while div < n:
	if n % div == 0:		# trovato un divisore
		print(n,"è divisibile per",div)
	div = div + 1			# proviamo con divisore successivo
