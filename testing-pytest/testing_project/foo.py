def add(a, b):
    print 'cucu'
    return a + b


def multiply(x, y):
    z = add(x, y)
    return z * 2


def is_prime(in_):
    return not bool(filter(lambda y: in_ % y == 0, range(2, in_)))


def test_true():
    assert True
