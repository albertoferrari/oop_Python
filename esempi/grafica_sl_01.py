'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di utilizzo delle funzioni grafiche del modulo g2d
'''
# importazione del modulo
import g2d

# Creazione del canvas, larghezza = 600 pixel, altezza = 400 pixel
g2d.init_canvas((600, 400))

# Rettangolo giallo, posizione angolo sinistra = 150, top = 100
# larghezza larghezza = 250, altezza = 200
# red=255 (max), green=255 (max), blue=0 (min)
g2d.set_color((255, 255, 0))         # color
g2d.fill_rect((150, 100, 250, 200))  # rect

# cerchio blu, centro = (400, 300), raggio = 20
g2d.set_color((0, 0, 255)) 		# impostazione colore
g2d.fill_circle((400, 300), 20)	# disegno del cerchio

# Ciclo di gestione eventi
g2d.main_loop()
