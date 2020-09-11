'''
Alberto Ferrari
Visualizzare tutti i divisori di un numero intero positivo
(controllare e richiedere) ricevuto in input
'''
#input
n = int(input("numero intero positivo: "))

while n <= 0:
    n = int(input("numero intero positivo: "))

'''
for div in range(1,n+1):        #div possibile divisore
    if n % div == 0:            #div è divisore di n
        print(n,"è divisibile per",div)
'''

div = 1
while div <= n:
    if n % div == 0:
        print(n,"è divisibile per",div)
    div = div + 1    


