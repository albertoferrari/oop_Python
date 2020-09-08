'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Si riceve come dato d'ingresso una sequenza di numeri interi, 
i numeri sono al massimo 10, non è conosciuta a priori la lunghezza 
di questa sequenza che termina o al raggiungimento del decimo valore 
o quando viene inserito il valore 0. 
Al termine dell’input si visualizzi la media aritmetica 
dei valori inseriti (non si consideri il valore 0 finale).
'''
n_ins = 0		# numero di valori già inseriti
somma = 0		# somma dei valori inseriti
n = float(input("inserisci un valore: "))


while n != 0 and n_ins < 9:
	n_ins += 1
	somma += n 
	n = float(input("inserisci un valore: "))
	
print("media dei valori inseriti",somma/n_ins)
