import unittest

from lesson13.ex1 import sort_int, sort_string, filter_dict


class TestClass(unittest.TestCase):

    def test_str(self):
        self.assertEqual(sort_string(['', 'fdfsd', 11, None, 'ddd']), ['fdfsd', 11, 'ddd'])

    def test_int(self):
        self.assertEqual(sort_int([1, 5, 2, 89, 3]), [1, 2, 3, 5, 89])

    def test_dict(self):
        self.assertEqual(filter_dict([{'id': 2, 'value': 25}, {'id':2, 'value': 0}, {'id': 2, 'value': 0},
                                      {'id': 2, 'value': 456}]), [{'id': 2, 'value': 25}, {'id': 2, 'value': 456}])

