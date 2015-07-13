import unittest

from .foo import add


class TestAddMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2, add(1, 1))

    def test_lt_zero(self):
        self.assertTrue(add(1, -2) < 0)
