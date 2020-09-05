'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Dato il perimetro di un quadrato, 
 fornire come risultato il valore del lato e dell’area
'''
# input
perimetro = float(input("perimetro del quadrato: "))
# elaborazione
lato = perimetro / 4
area = lato ** 2
#output
print("il quadrato con perimetro",perimetro)
print("ha il lato lungo",lato)
print("e l'area di superficie", area)
