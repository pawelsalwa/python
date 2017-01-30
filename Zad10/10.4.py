class Queue:

	def __init__(self):
		self.items = []

	def __str__(self):             # podgladanie kolejki
		return str(self.items)

	def is_empty(self):
		return not self.items

	def is_full(self):             # nigdy nie jest pusta
		return False

	def put(self, data):
		if self.is_full():
			raise ValueError("kolejka pelna")
		else:
			self.items.append(data)

	def get(self):
		if self.is_empty():
			raise ValueError("kolejka pusta")
		else:
			return self.items.pop(0)   # malo wydajne!

#===================test====================================
print 'start'

q = Queue()

print 'empty(): ' + repr(q.is_empty())
print 'full(): ' + repr(q.is_full())

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print q.get()
print q.get()
print q.get()
print q.get()

print 'empty(): ' + repr(q.is_empty())
print 'full(): ' + repr(q.is_full())


print 'koniec'








