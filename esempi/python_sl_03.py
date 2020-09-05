'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 somma valori da 1 a n
'''

n = int(input("quanti numeri vuoi sommare? "))

somma = 0		# accumulatore 
cont = 1		# valore da sommare

while cont <= n:
	# print("sto sommando il valore",cont)
	somma = somma + cont
	cont = cont + 1

print("la somma vale",somma)
