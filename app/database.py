"""Defines all the functions related to the database"""
from app import db
import sys

def fetch_cases(city_id: int, date: str) -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    todo_list = []

    if city_id == 0 and date == '':
        query_results = conn.execute("Select * from Cases WHERE num_cases > 9990 LIMIT 10;").fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "num_cases": result[2]
            }
            todo_list.append(item)

    elif city_id == -1 and date == 'query':
        query_results = conn.execute("SELECT SUM(ca.num_cases) as all_time_cases, ci.city_name FROM Cases ca NATURAL JOIN City ci GROUP BY ci.city_name ORDER BY all_time_cases DESC LIMIT 15;").fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_id": result[1],
                "date": 'All Time',
                "num_cases": result[0]
            }
            todo_list.append(item)

    else:
        query_results = conn.execute('SELECT * FROM Cases WHERE city_id = {} AND date = "{}";'.format(city_id, date)).fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "num_cases": result[2]
            }
            todo_list.append(item)

    return todo_list


def update_case_entry(city_id: int, date: str, cases_count: int) -> None:
    """Updates case description based on given `city_id` and `date`

    Args:
        city_id (int): Targeted city_id
        date (str): Targeted date
        cases_count (str): Updated number of cases

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update Cases set num_cases = {} where city_id = {} and date = "{}";'.format(cases_count, city_id, date)
    conn.execute(query)
    conn.close()


def insert_new_case(city_id: int, date: str, num_cases: int):
    """Insert new case to Cases table.

    Args:
        city_id (int): city id
        date (str): month of cases
        num_cases (int): number of cases for that month
    """

    conn = db.connect()
    query = 'Insert Into Cases (city_id, date, num_cases) VALUES ({}, "{}", {});'.format(
        city_id, date, num_cases)
    conn.execute(query)
    conn.close()



def remove_case(city_id: int, date: str) -> None:
    """ remove entries based on city ID and date """
    conn = db.connect()
    query = 'Delete From Cases where city_id={} and date="{}";'.format(city_id, date)
    conn.execute(query)
    conn.close()


def fetch_vaccines(vaccine_id: int, state: int) -> dict:
    """Reads all tasks listed in the todo table
    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    todo_list = []

    if vaccine_id == 0 and state == 0:
        query_results = conn.execute("Select * from Vaccine LIMIT 10;").fetchall()
        conn.close()
        for result in query_results:
            item = {
                "vaccine_id": result[0],
                "round_of_dose": result[1],
                "type": result[2]
            }
            todo_list.append(item)


    elif vaccine_id == -1 and state == -1:
        query_results = conn.execute("SELECT c.city_name, SUM(d.num_delivered) as totalVaccines FROM City c NATURAL JOIN Distributions d GROUP BY c.city_name, c.city_id HAVING totalVaccines <= ALL(SELECT SUM(d.num_delivered) FROM City c NATURAL JOIN Distributions d GROUP BY c.city_id);").fetchall()
        conn.close()
        for result in query_results:
            item = {
                "vaccine_id": "City name: " + str(result[0]),
                "round_of_dose": "",
                "type": "Num delivered: " + str(result[1])
            }
            todo_list.append(item)

    else:
        query_results = conn.execute('SELECT * FROM Vaccine WHERE vaccine_id = {};'.format(vaccine_id)).fetchall()
        conn.close()
        for result in query_results:
            item = {
                "vaccine_id": result[0],
                "round_of_dose": result[1],
                "type": result[2]
            }
            todo_list.append(item)

    return todo_list


def update_vaccine_entry(vaccine_id: int, type: str) -> None:
    """Updates task status based on given `task_id`
    Args:
        task_id (int): Targeted task_id
        text (str): Updated status
    Returns:
        None
    """

    conn = db.connect()
    query = 'Update Vaccine set type = "{}" where vaccine_id = {};'.format(type, vaccine_id)
    conn.execute(query)
    conn.close()


def insert_new_vaccine(vaccine_id: int, round_of_dose: int, vaccine_type: str):

    conn = db.connect()
    query = 'Insert Into Vaccine (vaccine_id, round_of_dose, type) VALUES ({}, {}, "{}");'.format(
        vaccine_id, round_of_dose, vaccine_type)
    conn.execute(query)
    conn.close()



def remove_vaccine(vaccine_id: int) -> None:
    """ remove entries based on city ID and date """
    conn = db.connect()
    query = 'Delete From Vaccine where vaccine_id={};'.format(vaccine_id)
    conn.execute(query)
    conn.close()


def fetch_distributions(city_id: int, date: str, type_param: str) -> dict:
    """Reads all tasks listed in the table
    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    todo_list = []
    if city_id == 0 and date == '':
        query_results = conn.execute("Select * FROM Distributions LIMIT 15;").fetchall()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "type": result[2],
                "num_delivered" : result[3]
            }
            todo_list.append(item)

    elif city_id == -1 and date == 'query':
        query_results = conn.execute("Select Distinct c.city_name, del.num_delivered, d.num_deaths From Distributions del Natural Join City c Join Deaths d on d.city_id = c.city_id Where d.num_deaths > (Select avg(num_deaths) From Deaths) and d.date Like '1/1/2021' and del.date Like '1/1/2021' and type = 'Moderna' Order By d.num_deaths desc Limit 15;").fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_name": result[0],
                "num_delivered": result[1],
                "num_deaths" : result[2]
               
               
            }
            todo_list.append(item)

    else:
        query_results = conn.execute('SELECT * FROM Distributions WHERE city_id = {} AND date = "{}" AND type = "{}";'.format(city_id, date, type_param)).fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "type": result[2],
                "num_delivered" : result[3]
            }
            todo_list.append(item)


    return todo_list


def update_distribution_entry(city_id: int, date: str, num_delivered: int, type_param:str) -> None:
    """Updates distribution description based on given `city_id` and `date`
    Args:
        city_id (int): Targeted city_id
        date (str): Targeted date
        num_delivered (str): Updated number of delivered doses
        type_param (str) : Targeted type
    Returns:
        None
    """
    conn = db.connect()
    query = 'Update Distributions set num_delivered = {} where city_id = {} and date = "{}" and type = "{}";'.format(num_delivered, city_id, date, type_param)
    conn.execute(query)
    conn.close()


def insert_new_distribution(city_id: int, date: str, num_delivered: int, type_param: str):
    """Insert new distribution to Distributions table.
    Args:
        city_id (int): city id
        date (str): month 
        num_delivered (int): number of vaccines delivered for that month
        type_param (str): type of dose
    """

    conn = db.connect()
    query = 'Insert Into Distributions (city_id, date, type, num_delivered) VALUES ({}, "{}", "{}", {});'.format(
        city_id, date, type_param, num_delivered)
    conn.execute(query)
    conn.close()



def remove_distribution(city_id: int, date: str, type_param:str) -> None:
    """ remove entries based on city ID and date """
    print(city_id)
    print(date)
    print(type_param)
    conn = db.connect()
    query = 'Delete From Distributions where city_id={} and date="{}" and type ="{}";'.format(city_id, date, type_param)
    conn.execute(query)
    conn.close()


def fetch_deaths(city_id: int, date: str) -> dict:
    """Reads all tasks listed in the deaths table
    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    todo_list = []

    if city_id == 0 and date == '':
        query_results = conn.execute("Select * FROM Deaths ORDER BY city_id LIMIT 1000;").fetchall()
        # conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "num_deaths": result[2]
            }
            todo_list.append(item)

    if city_id == -1 and date == 'query':
        query_results = conn.execute("SELECT c.city_name, SUM(d.num_deaths) as total_deaths FROM City c NATURAL JOIN Deaths d GROUP BY c.city_name,c.city_id HAVING total_deaths <= ALL(SELECT SUM(d.num_deaths)FROM City c NATURAL JOIN Deaths d GROUP BY c.city_id);").fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": 'All Time',
                "num_deaths": result[1]
            }
            todo_list.append(item)

    else:
        query_results = conn.execute('SELECT * FROM Deaths WHERE city_id = {} AND date = "{}";'.format(city_id, date)).fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "num_deaths": result[2]
            }
            todo_list.append(item)

    return todo_list


def update_death_entry(city_id: int, date: str, deaths_count: int) -> None:
    """Updates death description based on given `city_id` and `date`
    Args:
        city_id (int): Targeted city_id
        date (str): Targeted date
        deaths_count (str): Updated number of deaths
    Returns:
        None
    """

    conn = db.connect()
    query = 'Update Deaths set num_deaths = {} where city_id = {} and date = "{}";'.format(deaths_count, city_id, date)
    conn.execute(query)
    conn.close()


def insert_new_death(city_id: int, date: str, num_deaths: int):
    """Insert new death to Deaths table.
    Args:
        city_id (int): city id
        date (str): month of deaths
        num_deaths (int): number of deaths for that month
    """

    conn = db.connect()
    query = 'Insert Into Deaths (city_id, date, num_deaths) VALUES ({}, "{}", {});'.format(
        city_id, date, num_deaths)
    conn.execute(query)
    conn.close()



def remove_death(city_id: int, date: str) -> None:
    """ remove entries based on city ID and date """
    conn = db.connect()
    query = 'Delete From Deaths where city_id={} and date="{}";'.format(city_id, date)
    conn.execute(query)
    conn.close()


def fetch_safety() -> dict:
    """Reads all tasks listed in the todo table
    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    todo_list = []

    
    query_results = conn.execute("CALL Result();").fetchall()
    conn.close()
    for result in query_results:
        item = {
            "city_id": result[0],
            "city_name": result[1],
            "safety_rating": result[2]
        }
        todo_list.append(item)
    return todo_list
