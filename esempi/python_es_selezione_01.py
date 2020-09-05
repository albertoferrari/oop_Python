'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Sapendo che in un parcheggio ogni ora di sosta costa € 1.2 per le prime 3
 ore e € 2 per le successive, scrivere un programma che richiede il
 numero di ore di parcheggio e visualizza il totale da pagare.
'''

ore = int(input("numero di ore: "))

if ore <= 3:
	costo = ore * 1.2
else:
	costo = 3 * 1.2 + (ore - 3) * 2
	
print("per",ore,"ore il costo è",costo)

