from flask import Blueprint, current_app, jsonify, request

from lib import add, subtract, multiply, divide
from model import Project, Status


bp = Blueprint("api", __name__)


@bp.route("/add", methods=["GET"])
def add_route():
	first_num, second_num = request.json
	return jsonify(result=add(first_num, second_num))


@bp.route("/subtract", methods=["GET"])
def subtract_route():
	first_num, second_num = request.json
	return jsonify(result=subtract(first_num, second_num))


@bp.route("/multiply", methods=["GET"])
def multiply_route():
	first_num, second_num = request.json
	return jsonify(result=multiply(first_num, second_num))


@bp.route("/divide", methods=["GET"])
def divide_route():
	first_num, second_num = request.json
	return jsonify(result=divide(first_num, second_num))


@bp.route("/statuses", methods=["GET"])
def get_statuses():
	statuses = Status.query.all()
	return jsonify(result=[status.serialise() for status in statuses])


@bp.route("/projects", methods=["GET"])
def get_projects():
	projects = Project.query.all()
	return jsonify(result=[project.serialise() for project in projects])


@bp.route("/key", methods=["GET"])
def get_environ_key():
	return jsonify(key=current_app.config["ENVIRON_KEY"])
