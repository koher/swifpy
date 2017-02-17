from swifpy import Dictionary, Optional
import unittest


class TestDictionary(unittest.TestCase):
    def test_sample(self):
        dictionary = Dictionary({'a': 2, 'b': 3, 'c': 5})

        a: Optional[int] = dictionary['a']  # Optional(2)
        dictionary['d'] = 7
        count: int = dictionary.count  # 4

        for key, value in dictionary:
            print("%s -> %d" % (key, value))

        self.assertEqual(a, Optional(2))
        self.assertEqual(count, 4)
