def factorial(n):
	wynik  = 1
	for i in range(1 , n+1): 
		wynik = wynik * i
	return wynik

print factorial(6)
