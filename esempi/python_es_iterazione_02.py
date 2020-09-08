'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Scrivere un programma che riceve in input il valore n compreso 
fra 2 e 20 e visualizza il valore di tutte le n potenze di 2
'''

n = int(input("valore intero nell'intervallo [2,20] "))
# richiesta nuovo input se errato
while n < 2 or n > 20:
	print("valore errato")
	n = int(input("valore intero nell'intervallo [2,20] "))

esp = 0 	# primo esponente

while esp <= n:
	print("2 elevato a",esp,"=",2**esp)
	esp += 1
