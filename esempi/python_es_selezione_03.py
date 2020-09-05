'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Dati tre valori che rappresentano le misure dei lati di un triangolo
 controllare se si tratta effettivamente di un triangolo
 (https://it.wikipedia.org/wiki/Disuguaglianza_triangolare) e, in caso
 positivo determinare se si tratta di un triangolo scaleno, isoscele o
 equilatero
'''

l1 = float(input("lato 1: "))
l2 = float(input("lato 2: "))
l3 = float(input("lato 3: "))

# controllo ammissibilità
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
	print("non è un triangolo")
else:
	print("è un triangolo",end=" ")	# end=" " non va a capo ma inserisce spazio dopo print
	# controllo tipo di triangolo
	if l1 == l2 and l1 == l3:
		print("equilatero")
	elif l1 == l2 or l1 == l3 or l2 == l3:
		print("isoscele")
	else:
		print("scaleno")

