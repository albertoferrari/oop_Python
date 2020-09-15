'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio funzioni
'''

def stampa(nome):
	'''
	visualizza nome programmatore centrato 
	su 80 caratteri
	'''
	l_nome = len(nome)					# lunghezza nome
	l_ast = (80 - l_nome) // 2 - 1		# numero di asterischi
	ast = "*" * l_ast					# asterischi iniziali a finali
	print(ast + " " + nome + " " + ast)
	
def ipotenusa(a,b):
	c = (a ** 2 + b ** 2) ** 0.5
	return c
	
stampa("Inizio programma")
c1 = int(input("primo   cateto: "))
c2 = int(input("secondo cateto: "))
ip = ipotenusa(c1,c2)
print(ip)
stampa("Saluti e baci")
