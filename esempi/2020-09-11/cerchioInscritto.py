'''
Alberto Ferrari
Disegnare in un canvas di dimensione 600x600
un cerchio inscritto di colore casuale
'''
import g2d                  # libreria grafica
import random               # libreria per numeri casuali

g2d.init_canvas((600,600))  # impostazione canvas

r = random.randint(0,255)   # componente red (0,255)
g = random.randint(0,255)   # componente green
b = random.randint(0,255)   # componente blue
colore = (r,0,0)

centro = (300,300)          # centro del canvas
raggio = 300                # raggio del cerchio

g2d.set_color(colore)       # imposto il colore
g2d.fill_circle(centro,raggio) # disegno cerchio

g2d.main_loop()             # attesa eventi
