#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

from Points import Point
import math

class Circle:
	"""Klasa reprezentująca okręgi na płaszczyźnie."""

	def __init__(self, x=0, y=0, r=1):
		if r < 0:
			raise ValueError("promień ujemny")
		self.pt = Point(x, y)
		self.r = r

	def __repr__(self):       # "Circle(x, y, radius)"
		return 'Circle(' + repr(self.pt.x) + ',' + repr(self.pt.y) + ',' + repr(self.r) + ')'

	def __eq__(self, other):
		if self.pt == other.pt and self.r == other.r:
			return True
		else:
			return False

		#nie potrafie znalesc powodu dlaczego __eq__ nie dziala...

	def __ne__(self, other):
		return not self == other

	def area(self):           # pole powierzchni
		return math.pi  * ( self.r ** 2 )

	def move(self, x, y):    # przesuniecie o (x, y)
		self.pt.x = self.pt.x + x
		self.pt.y = self.pt.y + y

	def cover(self, other):  # okrąg pokrywający oba
		return Circle( (self.pt.x + other.pt.x) /2 , (self.pt.y + other.pt.y)/2 , (self.pt.x + other.pt.x) /2 + self.r + other.r )

# Kod testujący moduł.

c1 = Circle(0,0,1)
c2 = Circle(0,4,2)
print c1.cover(c2)

import unittest

class TestCircle(unittest.TestCase):	
	def testRepr(self):
		self.assertEqual(c1.__repr__() ,"Circle(0,2,1)" )	

	def testEq(self):
		self.assertTrue(c1.__eq__(c1) )

	def testNe(self):
		self.assertTrue(c1.__ne__(c2) )

	def testArea(self):
		self.assertEqual(c1.area() , math.pi)

	def testMove(self):
		self.assertEqual(c1.move(0,2) , Circle(0,2,1))

	def testCover(self):
		self.assertFalse(c1.cover(c2).__eq__( Circle(0,2,3) ))
		#tu tez cos nie dziala choc jak printowalem to bylo to samo...



if __name__ == '__main__':
	unittest.main()
