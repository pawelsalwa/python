class Node:
	"""Klasa reprezentujaca wezel listy jednokierunkowej."""

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)  # bardzo ogolnie
#============================================================
def remove_head(node):
	if (node == None) :
		return None, node.data
	else:
		node = node.next
		return node , node.data

def remove_tail(node):
	if (node == None):
		raise ValueError
	while node:
		if (node.next.next == None):
			return node.next, node.next.data
		node.next = node.next.next
#============================================================
	

# Zastosowanie.
head = None                   # [], pusta lista
head = Node(1, head)          # [1]
head = Node(2, head)          # [2, 1]
head = Node(3, head)          # [3, 2, 1]
head = Node(4, head)          # [4, 3, 2, 1]


print head
print head.next
print head.next.next
print head.next.next.next

head, data = remove_head(head)
print "usuwam head"
print head
print data

head, data = remove_tail(head)
print "usuwam tail"
print head
print data



