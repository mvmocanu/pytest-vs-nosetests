import json

from django.test import TestCase, Client, RequestFactory
import django_nose.tools as nt
from django.test.utils import override_settings

from .models import Station
from .connect import connect


class StationTestCase(TestCase):

    def setUp(self):
        self.weta_station = Station.objects.create(
            call_sign='weta', name='weta station')
        self.koth_station = Station.objects.create(
            call_sign='koth', name='koth station')
        self.other_station = Station.objects.create(
            call_sign='other', name='other station')

    def test_is_weta(self):
        nt.assert_true(self.weta_station.is_weta())
        nt.assert_false(self.koth_station.is_weta())
        nt.assert_false(self.other_station.is_weta())

    def test_is_koth(self):
        nt.assert_false(self.weta_station.is_koth())
        nt.assert_true(self.koth_station.is_koth())
        nt.assert_false(self.other_station.is_koth())


class HomePageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_homepage(self):
        response = self.client.get('/')
        data = json.loads(response.content)
        nt.assert_in('hello', data)
        nt.assert_equal('world', data['hello'])
        # new shit only in django-nose
        nt.assert_code(response, 200)

    def test_homepage_with_rf(self):
        request = self.factory.get('/')
        from .views import index
        response = index(request)
        self.assertEquals(200, response.status_code)


class ConnectTestCase(TestCase):

    @override_settings(DEBUG=True)
    def test_connect_false(self):
        self.assertFalse(connect())

    @override_settings(DEBUG=False)
    def test_connect_true(self):
        self.assertTrue(connect())
