#!/usr/bin/env python

import json

from flask import Flask, jsonify, request

from api import bp


def create_app(testing=False):
	app = Flask(__name__)
	app.debug = True
	if testing:
		app.testing = True

	app.register_blueprint(bp, url_prefix="/api/v1")

	return app
