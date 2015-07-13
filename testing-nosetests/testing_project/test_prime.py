import unittest
from nose_ittr import ittr, IttrMultiplier
import django_nose.tools as nt

from .foo import is_prime


class TestPrimesWithITTR(unittest.TestCase):
    __metaclass__ = IttrMultiplier

    @ittr(primes=[0, 1, 2, 3, 7, 11], not_primes=[4, 6, 8, 9])
    def test_with_ittr_primes(self):
        nt.assert_true(is_prime(self.primes))
        nt.assert_false(is_prime(self.not_primes))
