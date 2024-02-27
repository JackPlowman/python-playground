import os
import tempfile
from typing import Generator

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


@pytest.fixture()
def app() -> Generator:
    """Create and configure a new app instance for each test."""
    db_fd, db_path = tempfile.mkstemp()

    app = create_app(
        {
            "TESTING": True,
            "DATABASE": db_path,
        }
    )

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture()
def client(app: object) -> object:
    """Create a test client for the app."""
    return app.test_client()


@pytest.fixture()
def runner(app: object) -> object:
    """Create a test runner for the app."""
    return app.test_cli_runner()
