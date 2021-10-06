# import json
# from django.urls import reverse

# # Create your tests here.
# class TestAPICase():

#     def test_home(self):
#         res = self.api.get(reverse('home'))
#         assert res.status == '200 OK'
#         assert b'URL Shortener' in res.data

from django.test import Client, TestCase
from django.urls import reverse

from .models import Shortener

class BaseTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.shortener = Shortener.create_short_url("https://github.com/pearlhamilton/url-shortener/blob/main/shortener/urls/tests.py")

class TestBasicViews(BaseTestCase):
    c = Client()

    def test_home(self):
        res = self.c.get(reverse('home'))
        # self.assertContains(res, "URL Shortener")
        assert b"URL Shortener" in res.content

    def test_home_post(self):
        res = self.c.post(reverse('home'), {"long_url": "https://www.velotio.com/engineering-blog/use-pytest-fixtures-with-django-models"})
        self.assertContains(res, '<a href=')

    def test_create_short_url(self):
        shortener = Shortener.create_short_url("https://github.com/pearlhamilton/url-shortener/blob/main/shortener/urls/tests.py")
        assert len(shortener) == 5

