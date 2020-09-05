'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 valore assoluto esempio if
'''

#input valore
n = float(input("inserisci un valore: "))

#alternativa
if n > 0:
	print("il valore inserito è positivo")
	valAssuluto = n
else:
	print("il valore inserito è negativo")
	valAssuluto = -n

print("il valore assoluto di",n,"è",valAssuluto)
