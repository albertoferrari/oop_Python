'''
Prova intermedia
Scrivere un programma che genera un numero casuale compreso fra 40 e 59 
(estremi inclusi). Il numero rimane “segreto e non viene visualizzato”. 
Il programma richiede poi all’utente di inserire valori fino a quando 
“indovina” il numero generato. Infine visualizza il numero di tentativi effettuati per “indovinare” il numero. L’output finale sarà del tipo: 
Il numero generato è 48 ed è stato indovinato in 13 tentativi
'''

import random

segreto = random.randint(40,59)			# numero segreto
print("numero segreto",segreto)			# eliminare



n = int(input("inserisci un numero fra 40 e 59: "))
tentativi = 1							# tentativi effettuati

while n != segreto:						# errato
	print("numero errato ritenta",end = " ")
	n = int(input("inserisci un numero: "))
	tentativi = tentativi + 1			# incremento tentativi

print("hai indovinato il numero",segreto,"in",tentativi,"tentativi")
