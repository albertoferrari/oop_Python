'''
libreria grafica 3d
- min:max par f lista restituisce valore minimo e massimo della lista f
- ipotenusa par a,b (cateti) restituisce valore ipotenusa
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
	
def ipotenusa(a,b):
	c = (a ** 2 + b ** 2) ** 0.5
	return c
