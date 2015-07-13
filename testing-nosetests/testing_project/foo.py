def add(a, b):
    return a + b


def is_prime(in_):
    return not bool(filter(lambda y: in_ % y == 0, range(2, in_)))


def test_true():
    assert True
