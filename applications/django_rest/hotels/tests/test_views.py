from typing import Self
from unittest import TestCase

from hotels.views import HotelsApiView
import pytest


class TestHotelsApiView(TestCase):
    """Test case for the HotelsApiView view."""

    @pytest.mark.django_db
    def test_get(self: Self) -> None:
        view = HotelsApiView()
        response = view.get(None)
        assert response.status_code == 200
        assert response.data == []
