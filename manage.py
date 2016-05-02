#!/usr/bin/env python

from flask.ext.script import Manager

from app import create_app


app = create_app()
manager = Manager(app)


@manager.command
def runtests():
	import unittest
	suite = unittest.TestLoader().discover("tests")
	test_app = create_app(testing=True)
	with test_app.app_context():
		test_results = unittest.TextTestRunner().run(suite)


@manager.command
def runserver():
	app.run(port=7100)


if __name__ == "__main__":
	manager.run()
