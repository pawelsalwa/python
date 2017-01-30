
dic={ "I":1 , "V":5 , "X":10 , "L":50 , " C":100 , "D":500 , "M":1000 }

def roman2int(roman ):
	inty=[dic [liczba] for liczba in list(roman )]
	last = inty[0]
	i=1;

	while i< (len(inty)):
		if last < inty[i]:
			inty[i-1]=- inty[i-1]
		if(i<len(inty)):
			last=inty[i-1]
		i = i + 1

	return sum(inty)

x = raw_input("liczba rzymska do zamiany na int:?(duze litery) " )
print roman2int(x)
