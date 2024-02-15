from typing import Self

import pytest

from hotels.views import HotelsDetailApiView, HotelsListApiView


class TestHotelsListApiView:
    """Test case for the HotelsListApiView view."""

    @pytest.mark.django_db()
    def test_get(self: Self) -> None:
        view = HotelsListApiView()
        response = view.get(None)
        assert response.status_code == 200
        assert response.data == []

    @pytest.mark.django_db()
    def test_post(self: Self) -> None:
        view = HotelsListApiView()
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


class TestHotelsDetailApiView:
    """Test case for the HotelsDetailApiView view."""

    @pytest.mark.django_db()
    def test_get_hotel_not_found(self: Self) -> None:
        view = HotelsDetailApiView()
        request = type("Request", (), {"data": {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}})
        response = view.get(request, 1)
        assert response.status_code == 400
        assert response.data == {"response": "Object with hotel id does not exists"}

    @pytest.mark.django_db()
    def test_get(self: Self) -> None:
        view = HotelsListApiView()
        request = type("Request", (), {"data": {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}})
        response = view.post(request)
        hotel_id = response.data["id"]
        view = HotelsDetailApiView()
        request = type("Request", (), {"data": {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}})
        response = view.get(request, hotel_id)
        assert response.status_code == 200
        assert response.data["id"] == hotel_id
        response.data.pop("id")
        assert response.data == {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}
        assert response.data["name"] == "Hotel1"
        assert response.data["address"] == "Address1"
        assert response.data["phone"] == "Phone1"

    @pytest.mark.django_db()
    def test_put(self: Self) -> None:
        view = HotelsListApiView()
        request = type("Request", (), {"data": {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}})
        view.post(request)
        hotel_id = 1
        view = HotelsDetailApiView()
        request = type("Request", (), {"data": {"name": "Hotel2", "address": "Address2", "phone": "Phone2"}})
        response = view.put(request, hotel_id)
        assert response.status_code == 200
        assert response.data["id"] == hotel_id
        response.data.pop("id")
        assert response.data == {"name": "Hotel2", "address": "Address2", "phone": "Phone2"}
        assert response.data["name"] == "Hotel2"
        assert response.data["address"] == "Address2"
        assert response.data["phone"] == "Phone2"

    @pytest.mark.django_db()
    def test_delete(self: Self) -> None:
        view = HotelsListApiView()
        request = type("Request", (), {"data": {"name": "Hotel1", "address": "Address1", "phone": "Phone1"}})
        response = view.post(request)
        hotel_id = response.data["id"]
        view = HotelsDetailApiView()
        response = view.delete(None, hotel_id)
        assert response.status_code == 200
        response = view.get(None, hotel_id)
        assert response.status_code == 400
        assert response.data == {"response": "Object with hotel id does not exists"}
