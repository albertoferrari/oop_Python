'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 tetraedro
'''
# utilizzo libreria
import math
#input dato iniziale
spigolo = float(input("spigolo: "))
# calcolo del volume (errato come da testo)
# volume = 1/12 * spigolo * math.pow(2,1/3)
# calcolo del volume corretto
volume = 1/12 * math.pow(spigolo,3) * math.sqrt(2)
# output risultato
print("volume tetraedro con spigolo",spigolo,"=",volume)
