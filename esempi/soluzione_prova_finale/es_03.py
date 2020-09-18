'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Si vuole verificare se una data (giorno e mese) dell’anno 2020 
è corretta. Scrivere la funzione Python dataCorretta che riceve 
due parametri interi g e m che rappresentano il giorno e il mese 
e restituisce True se la data è corretta e False in caso contrario. 
Inserire la funzione in un programma che richiede in input un giorno 
e un mese e, utilizzando la funzione visualizza 
“data corretta” o “data non corretta”.
'''

def dataCorretta(g: int, m: int) -> bool:
	if m<1 or m>12:
		return False			#mese non corretto
	# impostazione giorni del mese
	'''
	Trenta giorni ha novembre con april, giugno e settembre.
	Di ventotto (29 bisestile) ce n'è uno,
	tutti gli altri ne han trentuno

	'''
	if m == 11 or m == 4 or m == 6 or m == 9:
		gm = 30
	elif m == 2:
		gm = 29
	else:
		gm = 31
	if g >= 1 and g <= gm:		# giorno corretto
		return True
	else:
		return False
		
def main():
	giorno = int(input("giorno: "))
	mese = int(input("mese: "))
	if dataCorretta(giorno, mese):
		print("data corretta")
	else:
		print("data non corretta")

main()
