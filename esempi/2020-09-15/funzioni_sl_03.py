'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio funzioni
'''

def dummy(f1, f2):
    loc = f1 ** f2
    f1 = f1 * 2
    return loc

a1 = float(input("fist value: "))
a2 = float(input("secondt value: "))
print(dummy(a1,a2))
print(loc)    # NameError: name 'loc' is not defined
print(a1) 	# print ???

