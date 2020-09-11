'''
Alberto Ferrari
canvas di 600x600 10 quadrati di colore casuale.
Il primo deve coprire completamente il canvas,
ogni successivo deve avere dimensione 5% inferiore al precedente.
'''
import g2d                  # libreria grafica
import random               # libreria per numeri casuali

g2d.init_canvas((600,600))  # impostazione canvas

dim = 600                   # larghezza e altezza rettangolo
x = 0                       # coordinata x
y = 0                       # coordinata y

for i in range(1,11):
    r = random.randint(0,255)   # componente red (0,255)
    g = random.randint(0,255)   # componente green
    b = random.randint(0,255)   # componente blue
    colore = (r,g,b)

    g2d.set_color(colore)       # imposto il colore
    g2d.fill_rect((x,y,dim,dim))   # disegno quadrato
    perc = int(dim*10/100)      # percentiuael diminuzione 
    dim = dim - perc            # modifica dimensione
    x = x + perc // 2           # modifica coordinate
    y = y + perc // 2

g2d.main_loop()             # attesa eventi
