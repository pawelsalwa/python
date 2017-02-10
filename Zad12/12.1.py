import random    

n = 100
k = 10
L = []

for i in range (n):    
    L.append(random.randint(0,k-1))

#print L

y = random.randint(0,k-1)

print 'y = ' + repr(y)
iloscWystapienY = 0;
listaIndeksow = []

for i in range(n):
	if(y == L[i]):
		iloscWystapienY += 1
		listaIndeksow.append(i) #poprawione

print iloscWystapienY
print listaIndeksow
