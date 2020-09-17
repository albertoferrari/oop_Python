'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di utilizzo di una classe
'''

import g2d
from sl04_01_Palla import Palla, ARENA_L, ARENA_H

def avanza():
    g2d.clear_canvas()  			# "pulisce il background
    p1.muovi()
    p2.muovi()
    g2d.set_color((0, 0, 255))		# colore prima palla
    g2d.fill_rect(p1.posizione())  	# disegno prima palla
    g2d.set_color((0, 255, 0))		# colore seconda palla
    g2d.fill_rect(p2.posizione())  	# disegno seconda palla
    
p1 = Palla(40, 80)						# movimento dx 5 dy 5
p2 = Palla(80, 40, 3, 2)				# movimento dx 3 dy 2

def main():
	g2d.init_canvas((ARENA_L, ARENA_H))
	g2d.main_loop(avanza, 1000 // 30)  # Millisecondi (frame rate)

if __name__ == "__main__":	# solo se è il modulo principale
	main()
