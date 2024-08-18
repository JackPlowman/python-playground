from unittest.mock import MagicMock, mock_open, patch

from flask_rest.database.utils import create_tables, run_query, run_script, set_up_database, set_up_test_data

FILE_PATH = "flask_rest.database.utils"
MOCK_DIR_PATH = "path"
QUERY = "query"


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


@patch("pathlib.Path.open", mock_open(read_data=QUERY))
@patch(f"{FILE_PATH}.connection")
def test_run_script(mock_connection: MagicMock) -> None:
    run_script("script_file_path")
    mock_connection.executescript.assert_called_once_with(QUERY)
    mock_connection.commit.assert_called_once()


@patch(f"{FILE_PATH}.connection")
def test_run_query(mock_connection: MagicMock) -> None:
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = "response"
    response = run_query(QUERY)
    assert response == "response"
    mock_connection.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once_with(QUERY, ())
    mock_cursor.fetchall.assert_called_once()
