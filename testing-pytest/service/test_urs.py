import pytest

from .urs import UrsService


def test_connect_with_exception():
    urs = UrsService('foo', 'bar')
    with pytest.raises(ValueError):
        urs.connect()


def test_urs_connect():
    urs = UrsService('dog', 'bar')
    assert urs.connect()


def test_redirect():
    urs = UrsService('dog', 'bar')
    assert urs.get_redirect('google.com') == 'http://google.com'
