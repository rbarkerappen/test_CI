#!/usr/bin/env python

import os
import sys

from flask.ext.script import Manager

from app import create_app, db
from config import environments

config = environments[os.environ.get("ENV", "dev")]
app = create_app(config)
manager = Manager(app)


def seed_db():
	from model import Status
	db.session.add(Status(name=Status.ACTIVE))
	db.session.add(Status(name=Status.DISABLED))
	db.session.add(Status(name=Status.CLOSED))
	db.session.commit()


@manager.command
def runtests():
	import unittest
	suite = unittest.TestLoader().discover("tests")
	test_app = create_app(environments["test"])
	with test_app.app_context():
		db.drop_all()
		db.create_all()
		seed_db()
		test_results = unittest.TextTestRunner().run(suite)
		sys.exit(not test_results.wasSuccessful())


@manager.command
def createschema():
	import model
	db.create_all()


@manager.command
def seed():
	seed_db()


@manager.command
def dropschema():
	import model
	db.drop_all()


@manager.command
def runserver():
	app.run(port=7100)


if __name__ == "__main__":
	manager.run()
