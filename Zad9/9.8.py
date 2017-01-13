class Node:
	"""Klasa reprezentujaca wezel drzewa binarnego."""

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)
#============================================================

def bst_max(top):
	if (top==None):
		raise ValueError

	while (top.right != None):
		top = top.right
	return top.data

def bst_min(top):
	if (top==None):
		raise ValueError

	while (top.left != None):
		top = top.left
	return top.data
#============================================================

top = Node(4)

top.left = Node(2)
top.left.left = Node(1)
top.left.right = Node(3)


top.right = Node(6)
top.right.right = Node(7)
top.right.left = Node(5)

print bst_max(top)#7
print bst_min(top)#1


