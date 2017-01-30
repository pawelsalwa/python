from random import randint

class RandomQueue:

	def __init__(self, size = 10 ):
		self.tab = []
		self.elements = 0
		self.size = size

	def insert(self, item):
		self.tab.append(item)
		self.elements = self.elements + 1

	def remove(self):	# zwraca losowy element
		los = randint(0 , self.elements - 1)
		tmp = self.tab[los]
		print 'remove: tab[' + repr(los) + ']'

		self.tab[los] = self.tab[self.elements-1]
		del self.tab[self.elements-1]
		self.elements = self.elements - 1
		
		return tmp

	def is_empty(self):
		return self.elements == 0

	def is_full(self):
		return self.elements == self.size

#==============test========================================
print 'start'

q = RandomQueue(10)
print 'empty(): ' + repr(q.is_empty())
print 'full(): ' + repr(q.is_full())

print q.elements
q.insert(1)
print q.elements
q.insert(2)
print q.elements
q.insert(3)
print q.elements
q.insert(4)
print q.elements

print q.remove()
print q.remove()
print q.remove()

print 'empty(): ' + repr(q.is_empty())
print 'full(): ' + repr(q.is_full())








