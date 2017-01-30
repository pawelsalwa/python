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

def p2( i , j ):
	dic = {}
	tmp = 0
	wy = 0
	if i==0 and j==0:
		dic[00] = 0.5
	elif j==0 and i>0:
		dic[00] = 0.0
	elif j>0 and i==0:
		dic[00] = 1.0
	else:
		for x in range(j+1):
			dic["0"+str(x)]=1.0
		for x in range(i+1):
			dic[str(x)+"0"]=0.0
		for x in range(1, i+1):
			for y in range(1, j+1):
				dic[str(x)+str(y)]=0.5*(dic[str(x-1)+str(y)]+dic[str(x)+str(y-1)])
	return dic[str(i)+str(j)]

print p1(5,3)#rekur
print p2(5,3)#iter
