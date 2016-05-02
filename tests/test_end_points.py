import json
import unittest

from flask import current_app

from app import db
from model import Project, Status


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

	def test_get_statuses(self):
		rv = self.test_client.get("/api/v1/statuses")
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.mimetype, "application/json")
		response_data = json.loads(rv.get_data().decode())
		self.assertIsInstance(response_data, dict)
		self.assertIn("result", response_data)
		result = response_data["result"]
		statuses = Status.query.all()
		expected = [s.serialise() for s in statuses]
		self.assertEqual(expected, result)

	def test_get_projects(self):
		
		# add test data
		active = Status.query.filter_by(name=Status.ACTIVE).one()
		project1 = Project(project_id=101, name="this is a test", status=active)
		project2 = Project(project_id=102, name="this is another test", status=active)
		db.session.add(project1)
		db.session.add(project2)
		db.session.flush()

		rv = self.test_client.get("/api/v1/projects")
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.mimetype, "application/json")
		response_data = json.loads(rv.get_data().decode())
		self.assertIsInstance(response_data, dict)
		self.assertIn("result", response_data)
		result = response_data["result"]

		expected = [project1.serialise(), project2.serialise()]
		self.assertEqual(expected, result)
