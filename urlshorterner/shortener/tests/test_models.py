import pytest

from shortener.models import Shortener

@pytest.fixture
def test_create_short_url():
    url = Shortener.objects.create_short_url(long_url="https://www.velotio.com/engineering-blog/use-pytest-fixtures-with-django-models")
    code = url.short_url.split("api/")
    assert len(code[1]) == 5 