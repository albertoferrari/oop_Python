'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
Scrivere un programma che riceve in input la temperatura misurata 
in gradi Fahrenheit e la fornisce in output convertita in 
gradi Celsius (https://it.wikipedia.org/wiki/Grado_Fahrenheit)
'''

f = float(input("temperatura in gradi Fahrenheit: "))
c = (f-32) / 1.8

print("temperatura equivalente in gradi Celsius",c)
