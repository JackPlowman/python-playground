from collections.abc import Generator

import pytest

from flask_rest.app import app


@pytest.fixture
def test_app() -> Generator:
    """Create and configure a new app instance for each test."""
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(test_app: object) -> object:
    """Create a test client for the app."""
    return test_app.test_client()
