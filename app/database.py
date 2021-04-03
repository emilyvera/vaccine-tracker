"""Defines all the functions related to the database"""
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Cases WHERE num_cases > 9990 LIMIT 10;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "city_id": result[0],
            "date": result[1],
            "num_cases": result[2]
        }
        todo_list.append(item)

    return todo_list


def update_case_entry(task_id: int, date: str, cases_count: int) -> None:
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


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
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



def remove_city(city_id: int, date: str) -> None:
    """ remove entries based on city ID and date """
    conn = db.connect()
    query = 'Delete From Cases where city_id={} and date="{}";'.format(city_id, date)
    conn.execute(query)
    conn.close()
