from typing import Self
from unittest import TestCase

import pytest

from hotels.models import Hotels


class TestHotels(TestCase):
    """Test case for the Hotels model."""

    @pytest.mark.django_db
    def test_attributes(self: Self) -> None:
        hotel1 = Hotels.objects.create(name="Hotel1", address="Address1", phone="Phone1")
        assert hotel1.id is not None
        assert Hotels._meta.get_field("id").primary_key
        assert Hotels._meta.get_field("id").serialize is False
        assert Hotels._meta.get_field("id").verbose_name == "ID"
        assert hotel1.name == "Hotel1"
        assert Hotels._meta.get_field("name").max_length == 100
        assert hotel1.address == "Address1"
        assert Hotels._meta.get_field("address").max_length == 100
        assert hotel1.phone == "Phone1"
        assert Hotels._meta.get_field("phone").max_length == 100

    @pytest.mark.django_db
    def test__str__(self: Self) -> None:
        hotel1 = Hotels.objects.create(name="Hotel1", address="Address1", phone="Phone1")
        assert str(hotel1) == "Hotel: Hotel1 Address: Address1"
