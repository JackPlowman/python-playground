from unittest.mock import MagicMock, patch

from flask_rest.database.queries import fetch_all_cars

FILE_PATH = "flask_rest.database.queries"


@patch(f"{FILE_PATH}.run_query")
def test_fetch_all_cars(mock_run_query: MagicMock) -> None:
    mock_run_query.return_value = values = [{"id": 1, "make": "Toyota", "model": "Corolla", "year": 2019}]
    response = fetch_all_cars()
    assert response == values
    mock_run_query.assert_called_once_with("SELECT * FROM models")
