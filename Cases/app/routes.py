""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper
from urllib.parse import unquote
import sys

@app.route("/delete/<int:city_id>/<path:date>", methods=['POST'])
def delete(city_id, date):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_city(city_id, unquote(date))
        result = {'success': True, 'response': 'Removed city for that date'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:city_id>/<path:date>", methods=['POST'])
def update(city_id, date):
    """ recieved post requests for entry updates """

    date = unquote(date)
    data = request.get_json()

    try:
        if "num_cases" in data:
            db_helper.update_case_entry(city_id, date, data["num_cases"])
            result = {'success': True, 'response': 'Number of cases Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create/<int:city_id>/<path:date>/<int:num_cases>", methods=['POST'])
def create(city_id, date, num_cases):
    """ recieves post requests to add new case """
    date = unquote(date)
    db_helper.insert_new_case(city_id, date, num_cases)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)