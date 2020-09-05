'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Si ricevono in input due numeri interi positivi determinare se il
 maggiore dei due è multiplo del minore
'''

v1 = int(input("valore 1: "))
v2 = int(input("valore 2: "))

if v1 > v2:
	vmax = v1
	vmin = v2
else:
	vmax = v2
	vmin = v1

if vmax % vmin == 0:			# % indica resto della divisione intera
	print(vmax,"è multiplo di",vmin)
else:
	print(vmax,"non è multiplo di",vmin)
