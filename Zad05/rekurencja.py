def factorial(n):
	wynik  = 1
	for i in range(1 , n+1): 
		wynik = wynik * i
	return wynik

print factorial(6)

def fibonacci(n):
	F1 = 1
	F2 = 2
	Fn = F1 + F2
	for i in range(3 , n+1):
		F1 = F2
		F2 = Fn
		Fn = F1 + F2
	return Fn
print fibonacci(6)
