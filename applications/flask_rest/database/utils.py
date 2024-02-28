import os
import sqlite3

connection = sqlite3.connect("cars.db", check_same_thread=False)
dir_path = os.path.dirname(os.path.realpath(__file__))


def set_up_database() -> None:
    """Set up the cars table."""
    create_tables()
    set_up_test_data()


def create_tables() -> None:
    """Create the cars table if it doesn't exist."""
    run_script(f"{dir_path}/data/schema.sql")


def set_up_test_data() -> None:
    """Set up test data for the cars table."""
    run_script(f"{dir_path}/data/test_data.sql")


def run_script(script: str) -> None:
    """Run a SQL script.

    Args:
        script (str): The SQL script to run.
    """
    with open(script) as file:
        query = file.read()
        connection.executescript(query)
        connection.commit()


def run_query(query: str, args: tuple = ()) -> list:
    """Execute a SQL query and return the results.

    Args:
        query (str): The SQL query to execute.
        args (tuple, optional): The arguments to pass to the query. Defaults to ().

    Returns:
        list: The results of the query.
    """
    with connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        return cursor.fetchall()
