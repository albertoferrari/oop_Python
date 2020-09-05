'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Si riceve in input un valore che rappresenta il voto ottenuto da uno
 studente. Se il voto è minore o uguale a 13 si visualizza “non ammesso”,
 se maggiore di 13 e minore di 18 “ammesso con riserva”, se maggiore di
 18 “ammesso”.
'''

voto = int(input("voto: "))

if voto <= 13:
	print("non ammesso")
elif 13 < voto < 18:
	print("ammesso con riserva")
elif voto > 18:
	print("ammesso") 


