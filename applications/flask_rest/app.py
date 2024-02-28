from flask import Flask

from .database.queries import fetch_all_cars
from .database.utils import set_up_database

app = Flask(__name__)


@app.route("/setup-cars", methods=["POST"])
def setup_cars() -> dict:
    """Retrieve all cars from the database.

    Returns:
        dict: A dictionary containing the list of cars.
    """
    set_up_database()
    return {"message": "Database set up successfully."}


@app.route("/cars", methods=["GET"])
def get_cars() -> dict:
    """Retrieve all cars from the database.

    Returns:
        dict: A dictionary containing the list of cars.
    """
    return {"cars": fetch_all_cars()}
