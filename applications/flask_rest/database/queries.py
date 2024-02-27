from .utils import connection


def fetch_all_cars() -> list:
    """Fetch all cars from the cars table.

    Returns:
        list: A list of all cars in the cars table.
    """
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM models")
        return cursor.fetchall()


def insert_car(make: str, model: str, year: int) -> None:
    """Insert a new car into the cars table.

    Args:
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year of the car.
    """
    with connection:
        connection.execute(
            """
            INSERT INTO cars (make, model, year) VALUES (?, ?, ?)
            """,
            (make, model, year),
        )
