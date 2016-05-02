import json
import unittest

from flask import current_app


class TestEndPoints(unittest.TestCase):

	def setUp(self):
		self.test_client = current_app.test_client()

	def test_add_end_point(self):
		data = json.dumps([5, 6])
		rv = self.test_client.get("/api/v1/add", data=data, content_type="application/json")
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.mimetype, "application/json")
		response_data = json.loads(rv.get_data().decode())
		self.assertIsInstance(response_data, dict)
		self.assertIn("result", response_data)
		result = response_data["result"]
		self.assertEqual(result, 11)
	
	def test_subtract_end_point(self):
		data = json.dumps([40, 3])
		rv = self.test_client.get("/api/v1/subtract", data=data, content_type="application/json")
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.mimetype, "application/json")
		response_data = json.loads(rv.get_data().decode())
		self.assertIsInstance(response_data, dict)
		self.assertIn("result", response_data)
		result = response_data["result"]
		self.assertEqual(result, 37)

	def test_multiply_end_point(self):
		data = json.dumps([2, 10])
		rv = self.test_client.get("/api/v1/multiply", data=data, content_type="application/json")
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.mimetype, "application/json")
		response_data = json.loads(rv.get_data().decode())
		self.assertIsInstance(response_data, dict)
		self.assertIn("result", response_data)
		result = response_data["result"]
		self.assertEqual(result, 20)

	def test_divide_end_point(self):
		data = json.dumps([15, 5])
		rv = self.test_client.get("/api/v1/divide", data=data, content_type="application/json")
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.mimetype, "application/json")
		response_data = json.loads(rv.get_data().decode())
		self.assertIsInstance(response_data, dict)
		self.assertIn("result", response_data)
		result = response_data["result"]
		self.assertEqual(result, 3)
