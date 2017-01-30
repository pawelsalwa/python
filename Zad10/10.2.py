#=================================================================
class Stack:
	def __init__(self, size=10):
		self.items = size * [None]		# utworzenie tablicy
		self.n = 0						# liczba elementow na stosie
		self.size = size

	def is_empty(self):
		return self.n == 0

	def is_full(self):
		return self.size == self.n

	def push(self, data):
		if self.is_full():
			raise ValueError("stos pelny")
		else:
			self.items[self.n] = data
			self.n = self.n + 1

	def pop(self):
		if self.is_empty():
			raise ValueError("stos pusty")
		else:
			self.n = self.n - 1
			data = self.items[self.n]
			self.items[self.n] = None	# usuwam referencje
		return data
#=================================================================

#kod testujacy:

print 'start'

stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
print 'czy pusty? ' + repr(stack.is_empty())
print 'czy pelny? ' + repr(stack.is_full())
#stack.push(4) - wyrzuci ValueError

print stack.pop()
print stack.pop()
print stack.pop()
#print stack.pop() - wyrzuci ValueError
print 'czy pusty? ' + repr(stack.is_empty())
print 'czy pelny? ' + repr(stack.is_full())

