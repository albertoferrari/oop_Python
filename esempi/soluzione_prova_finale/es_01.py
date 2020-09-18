'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Il “Sole 24 ore” fornisce i dati di cambio delle varie valute. 
Il giorno 17/09/2020 un Euro viene cambiato con 1.0859 Dollari USA e, 
nello stesso giorno un Dollaro USA viene cambiato con 1.0526 
Franchi svizzeri. 
Scrivere un programma Python che riceve in input un importo in Euro 
e visualizza l’importo equivalente in Dollari USA e in Franchi svizzeri. 
'''

euro = float(input("importo in Euro: "))

dolUSA = euro * 1.0859
frSUI = dolUSA * 1.0526

print("equivale a dollari USA",dolUSA)
print("e a ",frSUI,"franchi svizzeri")
