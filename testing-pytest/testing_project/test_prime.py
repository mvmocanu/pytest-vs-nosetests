import pytest

from .foo import is_prime


@pytest.mark.parametrize("number", [0, 1, 2, 3, 7, 9, 11])
def test_with_parametrize_primes(number):
    assert is_prime(number), 'fuck you biatch'


@pytest.mark.parametrize("number", [4, 6, 8, 9])
def test_with_parametrize_not_primes(number):
    assert not is_prime(number)
