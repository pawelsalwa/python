def flatten(sequence):
	for item in sequence:
		if isinstance(item,(list,tuple)):
			yield flatten(item)
		else:
			yield item

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

for i in flatten(seq):
	print i


#przy- yield flatten(item)- cos nie dziala w rekurencji
