from unittest.mock import MagicMock, patch

from flask_rest.database.utils import create_tables, set_up_database, set_up_test_data

FILE_PATH = "flask_rest.database.utils"
MOCK_DIR_PATH = "path"


@patch(f"{FILE_PATH}.create_tables")
@patch(f"{FILE_PATH}.set_up_test_data")
def test_set_up_database(mock_set_up_test_data: MagicMock, mock_create_tables: MagicMock) -> None:
    set_up_database()
    mock_create_tables.assert_called_once()
    mock_set_up_test_data.assert_called_once()


@patch(f"{FILE_PATH}.dir_path", MOCK_DIR_PATH)
@patch(f"{FILE_PATH}.run_script")
def test_create_tables(mock_run_script: MagicMock) -> None:
    create_tables()
    mock_run_script.assert_called_once_with(f"{MOCK_DIR_PATH}/data/schema.sql")


@patch(f"{FILE_PATH}.dir_path", MOCK_DIR_PATH)
@patch(f"{FILE_PATH}.run_script")
def test_set_up_test_data(mock_run_script: MagicMock) -> None:
    set_up_test_data()
    mock_run_script.assert_called_once_with(f"{MOCK_DIR_PATH}/data/test_data.sql")
