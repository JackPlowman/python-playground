from unittest.mock import MagicMock, patch

FILE_PATH = "flask_rest.app"


@patch(f"{FILE_PATH}.set_up_database")
def test_setup_cars(mock_set_up_database: MagicMock, client: object) -> None:
    response = client.post("/setup-cars")
    assert response.status_code == 200
    assert response.json == {"message": "Database set up successfully."}
    mock_set_up_database.assert_called_once()


@patch(f"{FILE_PATH}.fetch_all_cars")
def test_get_cars(mock_fetch_all_cars: MagicMock, client: object) -> None:
    mock_fetch_all_cars.return_value = []
    response = client.get("/cars")
    assert response.status_code == 200
    assert response.json == {"cars": []}
