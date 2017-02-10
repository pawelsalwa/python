#P(0, 0) = 0.5,
#P(i, 0) = 0.0 dla i > 0,
#P(0, j) = 1.0 dla j > 0,
#P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0

def p1( i , j ):
	if i<0 or j<0:
		raise ValueError("zle wartosci")
	if i==0 and j==0:
		return 0.5
	elif j==0 and i>0:
		return 0.0
	elif j>0 and i==0:
		return 1.0
	else:
		return 0.5 * ( p1(i-1.0, j)+ p1(i, j-1.0) )

def p2(i,j): #poprawiona metoda- zamiast slownika jest lista list- tablica dwuwymiarowa
	
	tab = [[0 for x in range(2)] for y in range(j)]
	

	P = {k: {0: 0} for k in range(1, i+1)}
	P[0] = {0: 0}

	for i in range(1, i+1):
		P[0][i] = 1.0

	for x in range(1, i+1):
		for y in range(1, j+1):
			P[x][y] = 0.5 * (P[x-1][y] + P[x][y-1])
	return P[i][j]



import timeit
#print "czas wykonania rekurencyjnej = ",  timeit.timeit( p1, number=1) nie wiem w jaki sposob przekazac argumenty do p1(). wtedy zobaczylibysmy zapewne, ze iteracyjny sposob jest szybszy
#print "czas wykonania iteracyjnej = ",  timeit.timeit( p2, number=1 )

print p1(5,3)#rekur
print p2(5,3)#iter
