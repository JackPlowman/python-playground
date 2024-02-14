from hotels.urls import urlpatterns


def test_urls() -> None:
    assert urlpatterns is not None
    assert len(urlpatterns) == 1
    assert urlpatterns.__getitem__(0).pattern._route == "hotels"
