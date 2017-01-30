import random
import math

def calc_pi(n=100):
	"""Obliczanie liczby pi metoda Monte Carlo. n oznacza liczbe losowanych punktow."""
	kolo = 0	
	for x in range(0, n):
		d = math.hypot(random.uniform(-0.5,0.5), random.uniform(-0.5,0.5)) #zwraca odleglosc miedzy 0.0 a losowym punktem kwadratu
		if d < 0.5:
			kolo += 1 #tutaj liczy ile razy losowa liczba trafila do kola
	return 4.0 * kolo / n #faktyczny stosunek trafien w kolo do trafien poza nim z uwzglednieniem kwadratu


print 'rozne przyblizenia pi, rosnaca dokladnosc:'
print calc_pi(50)
print calc_pi(100)
print calc_pi(200)
print calc_pi(500)
print calc_pi(1000)
print calc_pi(5000)
print calc_pi(10000)
print calc_pi(1000000)
