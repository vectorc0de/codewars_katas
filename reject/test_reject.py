import src.unittest
from main import reject

class TestRejectFunction(unittest.TestCase):

    def test_filter_even_numbers(self):
        self.assertEqual(reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0), [1, 3, 5])

    def test_filter_integers_from_mixed_list(self):
        self.assertEqual(reject(['a', 'b', 3, 'd'], lambda x: type(x) == int), ['a', 'b', 'd'])

    def test_filter_strings_from_mixed_list(self):
        self.assertEqual(reject(['a', 'b', 3, 'd'], lambda x: type(x) == str), [3])

    def test_empty_list(self):
        self.assertEqual(reject([], lambda x: x % 2 == 0), [])

    def test_all_rejected(self):
        self.assertEqual(reject([1, 3, 5], lambda x: x % 2 != 0), [])

    def test_none_rejected(self):
        self.assertEqual(reject([1, 2, 3], lambda x: x > 10), [1, 2, 3])

    def test_predicate_always_true(self):
        self.assertEqual(reject([1, 2, 3], lambda x: True), [])

    def test_predicate_always_false(self):
        self.assertEqual(reject([1, 2, 3], lambda x: False), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()