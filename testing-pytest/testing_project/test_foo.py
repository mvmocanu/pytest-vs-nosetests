import mock
from .foo import multiply


def caca():
    return 'pipi'


@mock.patch('testing_project.foo.add')
def test_add(mocked, client):
    mocked.return_value = 44
    assert 88 == multiply(2, 4)
    assert mocked.called
    x = client.get('/')
    assert x.status_code == 400
