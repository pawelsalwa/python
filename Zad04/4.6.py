def sum_seq(sequence):
	if isinstance(sequence , (list, tuple)):
		return  sum(map(sum_seq , sequence))
	return sequence

L=(1,2,3,[5,5])
print L
print sum_seq(L)


#===========ponizsze nie dziala, choc wyglada jakby bylo dobrze===========
#suma = 0
#def sum_seq(sequence):
#	global suma
#	for i in range(0, len(sequence) -1):
#		if isinstance(sequence[i] , (list,tuple)):
#			sum_seq(sequence[i])
#		else:
#			suma = suma + sum(sequence)
#	return suma
#
#L=(1,2,3 , [5,5])
#print sum(L)
#print L
#print sum_seq(L)
