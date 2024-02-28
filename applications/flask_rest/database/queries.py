from .utils import run_query


def fetch_all_cars() -> list:
    """Fetch all cars from the cars table.

    Returns:
        list: A list of all cars in the cars table.
    """
    return run_query("SELECT * FROM models")
