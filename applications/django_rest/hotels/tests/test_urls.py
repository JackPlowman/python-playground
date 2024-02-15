from hotels.urls import urlpatterns


def test_urls() -> None:
    assert urlpatterns is not None
    assert len(urlpatterns) == 2
    assert urlpatterns.__getitem__(0).pattern._route == "hotels"
    assert urlpatterns.__getitem__(1).pattern._route == "hotels/<int:hotel_id>/"
