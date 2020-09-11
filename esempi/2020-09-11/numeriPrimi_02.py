'''
Alberto Ferrari
Richiede un numero intero, stabilisce se questo è primo
'''

#input
n = int(input("numero intero positivo: "))

while n <= 0:
    n = int(input("numero intero positivo: "))

div = 2         #possibili divisori da 2 a n-1
primo = True    #per il momento il numero è primo

while div < n and primo == True:
    print("controllo divisore",div)
    if n % div == 0:            # ho trovato un divisore
        primo = False
    div = div +1

if primo == True:
    print(n,"è primo")
else:
    print(n,"non è primo")
        
