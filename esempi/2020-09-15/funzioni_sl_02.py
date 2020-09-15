'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio funzioni
'''

def ipotenusa(a,b):
	c = (a ** 2 + b ** 2) ** 0.5
	return c

def main():
	c1 = int(input("primo   cateto: "))
	c2 = int(input("secondo cateto: "))
	ip = ipotenusa(c1,c2)
	print(ip)

main()
