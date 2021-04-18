""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper
from urllib.parse import unquote
import sys

city_id_global = -1
date_global = ''

@app.route("/delete_case/<int:city_id>/<path:date>", methods=['POST'])
def delete_case(city_id, date):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_case(city_id, unquote(date))
        result = {'success': True, 'response': 'Removed city for that date'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit_case/<int:city_id>/<path:date>", methods=['POST'])
def update_case(city_id, date):
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


@app.route("/create_case/<int:city_id>/<path:date>/<int:num_cases>", methods=['POST'])
def create_case(city_id, date, num_cases):
    """ recieves post requests to add new case """
    date = unquote(date)
    db_helper.insert_new_case(city_id, date, num_cases)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/search_case/<int:city_id>/<path:date>", methods=['POST'])
def search_case(city_id, date):
    """ recieves post requests to add new case """
    global city_id_global
    global date_global
    date = unquote(date)
    city_id_global = city_id
    date_global = date
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/query_case", methods=['POST'])
def query_case():
    """ recieves post requests to add new case """
    global city_id_global
    global date_global
    city_id_global = -1
    date_global = "query"
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/cases")
def cases():
    global city_id_global
    global date_global
    items = []

    if city_id_global != -1 and date_global != '':
        items = db_helper.fetch_cases(city_id_global, date_global)
    elif city_id_global == -1 and date_global == 'query':
        items = db_helper.fetch_cases(city_id_global, date_global)
    else:
        items = db_helper.fetch_cases(0, '')

    city_id_global = -1
    date_global = ''

    return render_template("cases.html", items=items)


vaccine_id_global = -1
state_global = 0

@app.route("/delete_vaccine/<int:vaccine_id>", methods=['POST'])
def delete_vaccine(vaccine_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_vaccine(vaccine_id)
        result = {'success': True, 'response': 'Removed vaccine'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit_vaccine/<int:vaccine_id>", methods=['POST'])
def update_vaccine(vaccine_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "type" in data:
            db_helper.update_vaccine_entry(vaccine_id, data["type"])
            result = {'success': True, 'response': 'Status Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create_vaccine/<int:vaccine_id>/<int:round_of_dose>/<string:vaccine_type>", methods=['POST'])
def create_vaccine(vaccine_id, round_of_dose, vaccine_type):
    """ recieves post requests to add new task """
    # data = request.get_json()
    vaccine_type = unquote(vaccine_type)
    db_helper.insert_new_vaccine(vaccine_id, round_of_dose, vaccine_type)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/search_vaccine/<int:vaccine_id>", methods=['POST'])
def search_vaccine(vaccine_id):
    """ recieves post requests to add new case """
    global vaccine_id_global
    vaccine_id_global = vaccine_id
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/query_vaccine", methods=['POST'])
def query_vaccine():
    """ recieves post requests to add new case """
    global vaccine_id_global
    global state_global
    vaccine_id_global = -1
    state_global = -1
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/vaccines")
def vaccines():
    """ returns rendered homepage """
    global vaccine_id_global
    global state_global
    items = []

    if vaccine_id_global != -1 and state_global == 0:
        items = db_helper.fetch_vaccines(vaccine_id_global, state_global)
    elif vaccine_id_global == -1 and state_global == -1:
        items = db_helper.fetch_vaccines(vaccine_id_global, state_global)
    else:
    	items = db_helper.fetch_vaccines(0, 0)

    vaccine_id_global = -1
    state_global = 0

    return render_template("vaccines.html", items=items)

city_id_global2 = -1
date_global2 = ''
type_global2 = ''

@app.route("/delete_distribution/<int:city_id>/<path:date>/<string:type_param>", methods=['POST'])
def delete_distribution(city_id, date, type_param):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_distribution(city_id, unquote(date), unquote(type_param))
        result = {'success': True, 'response': 'Removed city distribution record for that date and type'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit_distribution/<int:city_id>/<path:date>/<string:type_param>", methods=['POST'])
def update_distribution(city_id, date, type_param):
    """ recieved post requests for entry updates """

    date = unquote(date)
    type_param = unquote(type_param)
    data = request.get_json()

    try:
        if "num_delivered" in data:
            db_helper.update_distribution_entry(city_id, date, data["num_delivered"], type_param)
            result = {'success': True, 'response': 'Number of Distributions Updated'}
            print(data["num_delivered"])
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    print(result)
    
    return jsonify(result)


@app.route("/create_distribution/<int:city_id>/<path:date>/<int:num_delivered>/<string:type_param>", methods=['POST'])
def create_distribution(city_id, date, num_delivered, type_param):
    """ recieves post requests to add new distribution """
    date = unquote(date)
    type_param = unquote(type_param)
    db_helper.insert_new_distribution(city_id, date, num_delivered, type_param)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/search_distribution/<int:city_id>/<path:date>/<string:type_param>", methods=['POST'])
def search_distribution(city_id, date, type_param):
    """ recieves post requests to search distribution """
    global city_id_global2
    global date_global2
    global type_global2
    date = unquote(date)
    city_id_global2 = 2
    type_global2 = unquote(type_param)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/query_distribution", methods=['POST'])
def query_distribution():
    """ recieves post requests to add new distribution """
    global city_id_global2
    global date_global2
    city_id_global2 = -1
    date_global2 = "query"
    type_global2 = ''
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/distributions")
def distributions():
    """ returns rendered homepage """
    global city_id_global2
    global date_global2
    global type_global2
    items = []

    if city_id_global2 != -1 and date_global2 != '':
        items = db_helper.fetch_distributions(city_id_global2, date_global2, type_global2)
    elif city_id_global2 == -1 and date_global2 == 'query':
        items = db_helper.fetch_distributions(city_id_global2, date_global2, type_global2)
    else:
        items = db_helper.fetch_distributions(0, '', type_global2)

    city_id_global2 = -1
    date_global2 = ''

    return render_template("vaccines.html", items=items)

city_id_global3 = -1
date_global3 = ''

@app.route("/delete_death/<int:city_id>/<path:date>", methods=['POST'])
def delete_death(city_id, date):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_death(city_id, unquote(date))
        result = {'success': True, 'response': 'Removed city death record for that date'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit_death/<int:city_id>/<path:date>", methods=['POST'])
def update_death(city_id, date):
    """ recieved post requests for entry updates """

    date = unquote(date)
    data = request.get_json()

    try:
        if "num_deaths" in data:
            db_helper.update_death_entry(city_id, date, data["num_deaths"])
            result = {'success': True, 'response': 'Number of deaths Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create_death/<int:city_id>/<path:date>/<int:num_deaths>", methods=['POST'])
def create_death(city_id, date, num_deaths):
    """ recieves post requests to add new death """
    date = unquote(date)
    db_helper.insert_new_death(city_id, date, num_deaths)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/search_death/<int:city_id>/<path:date>", methods=['POST'])
def search_death(city_id, date):
    """ recieves post requests to search death """
    global city_id_global3
    global date_global3
    date = unquote(date)
    city_id_global3 = city_id
    date_global3 = date
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/query_death", methods=['POST'])
def query_death():
    """ recieves post requests to add new death """
    global city_id_global3
    global date_global3
    city_id_global3 = -1
    date_global3 = "query"
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/deaths")
def deaths():
    """ returns rendered homepage """
    global city_id_global3
    global date_global3
    items = []

    if city_id_global3 != -1 and date_global3 != '':
        items = db_helper.fetch_deaths(city_id_global3, date_global3)
    elif city_id_global3 == -1 and date_global3 == 'query':
        items = db_helper.fetch_deaths(city_id_global3, date_global3)
    else:
        items = db_helper.fetch_deaths(0, '')

    city_id_global3 = -1
    date_global3 = ''

    return render_template("deaths.html", items=items)

@app.route("/safety", methods=['POST'])
def safety():
    """ returns rendered homepage """
    global city_id_global3
    global date_global3
   

    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = []
    items = db_helper.fetch_safety()
    return render_template("home.html",items=items)