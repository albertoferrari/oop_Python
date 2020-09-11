'''
Alberto Ferrari
Richiede un numero intero, stabilisce se questo è primo
'''

#input
n = int(input("numero intero positivo: "))

while n <= 0:
    n = int(input("numero intero positivo: "))

#conto i divisori
numDivisori = 0             # numero dei divisori di n

for div in range(1,n+1):                #div possibile divisore
    print("controllo divisore",div)
    if n % div == 0:                    #div è divisore di n
        print(n,"è divisibile per",div,)
        numDivisori = numDivisori + 1   #incremento il numero di divisori
        print("ho trovato",numDivisori,"divisori")

# verifico il numero di divisori (se n è primo)
if numDivisori == 2:
    print(n,"è primo")
else:
    print(n,"non è primo")
