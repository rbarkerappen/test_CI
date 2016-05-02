#!/usr/bin/env python

import json

from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)

	db.init_app(app)
	
	from api import bp
	app.register_blueprint(bp, url_prefix="/api/v1")

	return app
