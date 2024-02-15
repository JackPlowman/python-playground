from typing import Self
from unittest import TestCase

import pytest

from hotels.views import HotelsApiView


class TestHotelsApiView(TestCase):
    """Test case for the HotelsApiView view."""

    @pytest.mark.django_db()
    def test_get(self: Self) -> None:
        view = HotelsApiView()
        response = view.get(None)
        assert response.status_code == 200
        assert response.data == []

    @pytest.mark.django_db()
    def test_post(self: Self) -> None:
        view = HotelsApiView()
        request = type("Request", (), {"data": {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}})
        response = view.post(request)
        assert response.status_code == 201
        assert response.data["id"] is not None
        assert response.data["id"] > 0
        response.data.pop("id")
        assert response.data == {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}
        assert response.data["name"] == "Hotel1"
        assert response.data["address"] == "Address1"
        assert response.data["phone"] == "Phone1"
