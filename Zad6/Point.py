import math

class Point:
	"""Klasa reprezentujaca punkty na plaszczyznie."""
	def __init__(self, x=0, y=0):  # konstuktor
		self.x = x
		self.y = y

	def __str__(self):
		return "("+repr(self.x)+", "+repr(self.y)+")"

	def __repr__(self):        # zwraca string "Point(x, y)"
		return self.__class__.__name__ + "("+repr(self.x)+", "+repr(self.y)+")"

	def __eq__(self, other):   # obsluga point1 == point2
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

	def __ne__(self, other):   # obsluga point1 != point2
		if self.x != other.x or self.y != other.y:
			return True
		else:
			return False
#=======================Punkty jako wektory 2D===================================

	def __add__(self, other):  # v1 + v2
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other): # v1 - v2
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other): # v1 * v2, iloczyn skalarny
		return self.x * other.x + self.y * other.y

	def cross(self, other):	# v1 x v2, iloczyn wektorowy 2D
		return self.x * other.y - self.y * other.x
		#return Point(self.x * other.y, self.y * other.x)

	def length(self): # dlugosc wektora
		return math.sqrt(self.x ** 2.0 + self.y ** 2.0)
#================================================================================
#Kod testujacy modul

p1 = Point(2,3)
p2 = Point(3,4)
 
import unittest
 
class TestPoint(unittest.TestCase):
#================================================================================
	def test__str__(self):
		self.assertEqual(p1.__str__(),"(2, 3)")
	def test__repr__(self):
		self.assertEqual(p1.__repr__(),"Point(2, 3)")
	def test__eq__(self):
		self.assertFalse(p1.__eq__(p2))
	def test__ne__(self):
		self.assertTrue(p1.__ne__(p2))

	def test__add__(self):
		self.assertEqual(p1.__add__(p2),Point(5,7))
	def test__sub__(self):
		self.assertEqual(p1.__sub__(p2),Point(-1,-1))
	def test__mul__(self):
		self.assertEqual(p1.__mul__(p2),18)
	def testcross(self):
		self.assertEqual(p1.cross(p2),-1)
	def testlength(self):
		self.assertEqual(p1.length(),math.sqrt(13))
#================================================================================

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy

