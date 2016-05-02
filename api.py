from flask import Blueprint, jsonify, request

from lib import add, subtract, multiply, divide


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
