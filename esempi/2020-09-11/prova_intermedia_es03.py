'''
Prova intermedia
Definire un canvas di dimensione 300x300.
Visualizzare 5 righe di cerchi, allineate a sinistra. 
Il numero di riga corrisponde al numero di cerchi da disegnare. 
Ogni cerchio ha il raggio di 20 pixel e un colore casuale.
'''

import g2d,random 				# libreria grafica e numeri casuali
	
g2d.init_canvas((300,300))

for riga in range(0,5):
	# posizione primo cerchio della riga
	yCentro = 20 + 40 * riga	# ogni riga è alta 40 pixel
	
	# in ogni riga n cerchi (1,2,3,4,5)
	for c in range(0,riga+1):
		# colore casuale ----------
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		colore = (r,g,b)
		g2d.set_color(colore)
		# --------------------------
		xCentro = 20 + 40 * c
		g2d.fill_circle((xCentro,yCentro),20)

g2d.main_loop()             # attesa eventi

