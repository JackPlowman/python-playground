from hotels.urls import urlpatterns


def test_urls() -> None:
    assert urlpatterns is not None
    assert len(urlpatterns) == 1
