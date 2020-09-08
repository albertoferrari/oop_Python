'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Scrivere un programma che riceve in input un valore intero compreso 
fra 2 e 10 e stampa la “tabellina” di quel numero (prodotti da 1 a 10)

'''
n = 0
while n<2 or n>10:
	n = int(input("inserisci un valore nellintervallo [2,10] "))

x = 1
while x<=10:
	print(n*x)
	x += 1
