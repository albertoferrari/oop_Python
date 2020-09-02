'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 conversione litri galloni
'''

litri = float(input("litri: "))

galIng = litri / 4.54609
galUSA = litri / 3.785411784

print("galloni inglesi",galIng)
print("galloni americani",galUSA)
