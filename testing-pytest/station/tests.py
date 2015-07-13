import pytest
import json

from .models import Station
from .connect import connect

foo = 'spam'


@pytest.fixture(scope="function")
def weta_station(request, db):
    station = Station.objects.create(
        call_sign='weta', name='weta station')
    return station


@pytest.fixture(scope="function")
def koth_station(db):
    return Station.objects.create(
        call_sign='koth', name='koth station')


@pytest.fixture(scope="function")
def other_station(db):
    return Station.objects.create(
        call_sign='other', name='other station')


@pytest.fixture(scope="function")
def stations(weta_station, koth_station, other_station):
    return weta_station, koth_station, other_station


def test_is_weta(stations):
    weta, koth, other = stations
    assert weta.is_weta()
    assert not koth.is_weta()
    assert not other.is_weta()


def test_is_koth(stations):
    weta, koth, other = stations
    assert not weta.is_koth()
    assert koth.is_koth()
    assert not other.is_koth()


def test_homepage(client):
    response = client.get('/')
    data = json.loads(response.content)
    assert 'hello' in data
    assert 'world' == data['hello']
    assert 200 == response.status_code


def test_homepage_with_rf(rf):
    request = rf.get('/')
    from .views import index
    response = index(request)
    assert 200 == response.status_code


def test_connect_true(settings):
    settings.DEBUG = False
    assert connect()


def test_connect_false(settings):
    settings.DEBUG = True
    assert not connect()
