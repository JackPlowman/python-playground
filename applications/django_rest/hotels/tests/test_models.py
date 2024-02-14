from typing import Self
from unittest import TestCase

from hotels.models import Hotels
import pytest


class TestHotels(TestCase):
    """Test case for the Hotels model."""

    @pytest.mark.django_db
    def test_attributes(self: Self) -> None:
        hotel1 = Hotels.objects.create(name="Hotel1", address="Address1", phone="Phone1")
        assert hotel1.id is not None
        assert hotel1.name == "Hotel1"
        assert hotel1.address == "Address1"
        assert hotel1.phone == "Phone1"

    @pytest.mark.django_db
    def test__str__(self: Self) -> None:
        hotel1 = Hotels.objects.create(name="Hotel1", address="Address1", phone="Phone1")
        assert str(hotel1) == "Hotel: Hotel1 Address: Address1"
