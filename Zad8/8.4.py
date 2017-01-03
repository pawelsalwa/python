from math import sqrt

def heron(a, b, c):
	"""Obliczanie pola powierzchni trojkata za pomoca wzoru
	Herona. Dlugosci bokow trojkata wynosza a, b, c."""

	if a + b < c or a + c < b or c + b < a:
		raise ValueError("boki nie tworza trojkata")
	return sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c)) / 4


print heron(3.0,4.0,5.0)
print heron(6.0,8.0,10.0)
print heron(6.0,8.0,100.0)
