import unittest

from lib import add, subtract, multiply, divide


class TestLib(unittest.TestCase):

	def test_add(self):
		self.assertEqual(add(2,3), 5)
		self.assertEqual(add(6,8), 14)

	def test_subtract(self):
		self.assertEqual(subtract(8,4), 4)
		self.assertEqual(subtract(2,3), -1)

	def test_multiply(self):
		self.assertEqual(multiply(4,5), 20)
		self.assertEqual(multiply(2,8), 16)

	def test_divide(self):
		self.assertEqual(divide(10,2), 5)
		self.assertEqual(divide(24,3), 8)
