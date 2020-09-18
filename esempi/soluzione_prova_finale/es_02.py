'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Per verificare il corretto bilanciamento di un dado da gioco con 
20 facce si effettuano 20000 lanci e si conteggia il numero di volte 
in cui è uscito il numero 12. Un risultato accettabile dovrebbe essere 
in un intorno di 1000 … Nonostante questo metodo sia sicuramente poco 
scientifico lo si vuole simulare con un programma Python 
che genera 20000 volte un valore compreso nell’intervallo [1,20], 
conta quante volte il numero generato è uguale a 12 
e al termine visualizza questo conteggio. 
'''

import random

n12 = 0			# numero di volte in cui è uscito 12

for l in range(1,20001):				# 20 mila volte
	faccia = random.randint(1,20)		# risultato lancio
	if faccia == 12:
		n12 = n12 + 1
		
print("il numero 12 è uscito",n12,"volte")
