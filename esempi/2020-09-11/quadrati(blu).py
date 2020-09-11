'''
Alberto Ferrari
canvas di 600x600 10 quadrati di colore casuale.
Il primo deve coprire completamente il canvas,
ogni successivo deve avere dimensione 5% inferiore al precedente.
'''
import g2d                  # libreria grafica

g2d.init_canvas((600,600))  # impostazione canvas

dim = 600                   # larghezza e altezza rettangolo
x = 0                       # coordinata x
y = 0                       # coordinata y

r = 0
g = 0
b = 255

for i in range(1,11):
    colore = (r,g,b)

    g2d.set_color(colore)       # imposto il colore
    g2d.fill_rect((x,y,dim,dim))   # disegno quadrato
    perc = int(dim*10/100)      # percentiuael diminuzione
    perc = 50
    dim = dim - perc            # modifica dimensione
    x = x + perc // 2           # modifica coordinate
    y = y + perc // 2
    b = b - perc

g2d.main_loop()             # attesa eventi
