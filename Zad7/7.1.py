#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

from fractions import gcd
#=================================================================
class Frac:
	"""Klasa reprezentująca ułamki."""

	def __init__(self, x=0, y=1):
		if y==0:
			raise FractionError("Divide by 0 error")
		else:
			# Sprawdzamy, czy y=0.
			self.x = x
			self.y = y
			self.skroc()

	def skroc(self):
		nwd = gcd(self.x,self.y)
		self.x = self.x / nwd
		self.y = self.y / nwd
 
	def __str__(self):         # zwraca "x/y" lub "x" dla y=1
		self.skroc()
		if self.y!=1:
			return repr(self.x) + '/' + repr(self.y)
		else:
			return repr(self.x)

	def __repr__(self):        # zwraca "Frac(x, y)"
		self.skroc()
		return 'Frac(' + repr(self.x) + ',' + repr(self.y) + ')'

	def __cmp__(self, other):  # porównywanie
		self.skroc()
		other2 = Frac()
		if other != type(Frac):
			other2 = Frac(other , 1)
		other2.skroc()
		if self.x == other2.x and self.y == other2.y:
			return True
		else:
			return False

	def __add__(self, other):  # frac1+frac2, frac+int
		nww = self.y * other.y / gcd(self.y  , other.y)
		mianownik = nww
		licznik = self.x * nww / self.y + other.x * nww / other.y
		nowy = Frac(licznik, mianownik)
		nowy.skroc()
		return nowy

	__radd__ = __add__              # int+frac

	def __sub__(self, other): # frac1-frac2, frac-int
		nww = self.y * other.y / gcd(self.y  , other.y)
		mianownik = nww
		licznik = self.x * nww / self.y - other.x * nww / other.y
		nowy = Frac(licznik, mianownik)
		nowy.skroc()
		return nowy

	def __rsub__(self, other):      # int-frac
		# tutaj self jest frac, a other jest int!
		return Frac(self.y * other - self.x, self.y)

	def __mul__(self, other): # frac1*frac2, frac*int
		nowy = Frac(self.x * other.x , self.y * other.y)
		nowy.skroc()
		return nowy

	__rmul__ = __mul__              # int*frac

	def __div__(self, other):  # frac1/frac2, frac/int
		nowy = Frac(self.x * other.y , self.y * other.x)
		nowy.skroc()
		return nowy

	def __rdiv__(self, other): # int/frac
		nowy = Frac(self * other.y, other.x)
		return nowy
    # operatory jednoargumentowe
	def __pos__(self):  # +frac = (+1)*frac
		return Frac(self.x,self.y)

	def __neg__(self):         # -frac = (-1)*frac
		return Frac(-self.x,self.y)

	def __invert__(self):      # odwrotnosc: ~frac
		return Frac(self.y,self.x)

	def __float__(self):    # float(frac)
		return float(self.x) / float(self.y)
#=================================================================
# Kod testujący moduł.

f1 = Frac(1,2)
f2 = Frac(1,4)
#=================================================================
import unittest
class TestFrac(unittest.TestCase):
	def setUp(self): pass

	def test_str(self):
		self.assertEqual(f1.__str__(),"1/2")

	def test_repr(self):
		self.assertEqual(f1.__repr__(),"Frac(1,2)")

	def test_add(self):
		self.assertEqual(f1.__add__(f2), Frac(3,4) )

	def test_sub(self):
		self.assertEqual(f1.__sub__(f2), Frac(1,4) )

	def test_mul(self):
		self.assertEqual(f1.__mul__(f2), Frac(1,8) )

	def test_div(self):
		self.assertEqual(f1.__div__(f2), Frac(2,1) )

	def test_pos(self):
		self.assertTrue(f1 == f1.__pos__() )

	def test_neg(self):
		self.assertEqual(f1.__neg__() , Frac(-1,2) )

	def test_invert(self):
		self.assertEqual(f1.__invert__() , Frac( 2, 1) )

	def test_float(self):
		self.assertEqual(f1.__float__() , 0.5)

if __name__ == '__main__':
	unittest.main()

