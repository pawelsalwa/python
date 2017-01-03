#mamy a * x + b * y + c = 0
#przedstawia ono linie prosta o parametrach a,b,c
#upraszczam problem:
#algorytm szukania miejsca zerowego prostej y = a*x + b
#gdzie mamy zadane a i b:


def solve1(a, b):
	"""Rozwiazywanie rownania liniowego  y = a*x + b ."""
	if a==0:
		if b==0:
			print 'rownanie ma nieskonczenie wiele rozwiazan'
			return
		else:
			print 'rownanie sprzeczne'
			return
	else:
		x = float(-b)/float(a)
		print 'rozwiazanie rownania: x = ' , x
	return



solve1(2,3)
solve1(15,5)
solve1(0,2)
solve1(0,0)

# uzylem schematu blokowego algorytmu z ponizszej strony
# http://alg24.com/images/Algorytmy/alg_rownlin.png

