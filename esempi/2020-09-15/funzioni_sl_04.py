'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio funzioni
'''

def min_max(f):
	'''
	restituisce valore minimo e massimo della lista f
	'''
	minimo 	= f[0]   # f[0] primo valore di f
	massimo = f[0]
	for i in range(1,len(f)):
		if f[i] < minimo:
			minimo = f[i]
		if f[i] > massimo:
			massimo = f[i]
	return minimo, massimo

def main():
	a = [2,-13,55,-3,8]
	x , y = min_max(a)
	print("minimo: ",x," massimo: ",y)

main()  ## remove if importing the module elsewhere


