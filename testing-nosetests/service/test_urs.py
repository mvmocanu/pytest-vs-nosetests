from django.test import TestCase

from .urs import UrsService


class UrsTestCase(TestCase):

    def test_connect_with_exception(self):
        urs = UrsService('foo', 'bar')
        with self.assertRaises(ValueError):
            urs.connect()

    def test_urs_connect(self):
        urs = UrsService('dog', 'bar')
        self.assertTrue(urs.connect())

    def test_redirect(self):
        urs = UrsService('dog', 'bar')
        self.assertEquals(urs.get_redirect('google.com'), 'http://google.com')
