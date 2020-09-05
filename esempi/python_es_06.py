'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Scrivere un programma che chiede all’utente il raggio di base 
 e l’altezza di un cilindro poi calcola e visualizza il volume (V =πr2h)
'''

import math

raggio = float(input("raggio di base: "))
altezza = float(input("altezza: "))

volume = math.pi * raggio * 2 * altezza

print("volume",volume)
