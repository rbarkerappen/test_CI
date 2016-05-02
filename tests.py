#!/usr/bin/env python3

import unittest

from lib import add, subtract, multiply, divide


class TestCases(unittest.TestCase):

	def test_add(self):
		assert add(2,3) == 5
		assert add(6,8) == 14

	def test_subtract(self):
		assert subtract(8,4) == 4
		assert subtract(2,3) == -1

	def test_multiply(self):
		assert multiply(4,5) == 20
		assert multiply(2,8) == 16

	def test_divide(self):
		assert divide(10,2) == 5
		assert divide(24,3) == 8


if __name__ == "__main__":
	unittest.main()
