'''
Prova intermedia
Chiedere all'utente un numero intero positivo n compreso fra 10 e 20 
(richiedere se valore non corretto). 
Disegnare n quadrati tutti con lato di 100 pixel ciascuno in posizione casuale
ciascuno con un colore casuale. 
(suggerimento: cominciare a disegnare un solo quadrato grigio, in posizione casuale)
'''

import g2d,random 				# libreria grafica e numeri casuali

n = int(input("inserire un numero compreso fra 10 e 20: "))

while n < 10 or n > 20:
	n = int(input("inserire un numero compreso fra 10 e 20: "))
	
g2d.init_canvas((600,600))

for i in range(1,n+1):
	# colore casuale ----------
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	colore = (r,g,b)
	g2d.set_color(colore)
	# --------------------------

	# posizione casuale --------
	x = random.randint(0,500)
	y = random.randint(0,500)
	# --------------------------

	# disegno quadrato ---------
	g2d.fill_rect((x,y,100,100))
	# --------------------------

g2d.main_loop()             # attesa eventi

