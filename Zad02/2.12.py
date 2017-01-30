line = 'asd\n		asd \n asd'

lista = line.split() #tworzymy liste z wielowierszowego
nowy = ""

for znak in lista:
	nowy = nowy + znak[0] #pierwsze wyrazy listy
print nowy

nowy = ""
for ch in lista:
	nowy = nowy + znak[-1:] # ostatnie wyrazy listy
print nowy



del line
del lista
del nowy
