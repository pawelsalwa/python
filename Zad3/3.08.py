L1=['a','b','c','d']
L2=['x','a','y','z','d']

i,j =0,0

L3 = []

while( i< len(L1)):
	while (j < len(L2)):
		if (L1[i] == L2[j]):
			L3.append(L2[j])
		j = j+1
	i=i+1


print L3 #cos nie dziala

i,j =0,0

L4 = []

while( i< len(L1)):
	L4.append(L1[i])
	while (j < len(L2)):
		if (L1[i] != L2[j]):
			L4.append(L2[j])
		j = j+1
	i=i+1

print L4





