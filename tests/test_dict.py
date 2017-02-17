from .context import swifpy as k
import unittest


class TestDict(unittest.TestCase):
    def test_sample(self):
        dictionary = k.dict(('a', 2), ('b', 3), ('c', 5))
        # dictionary = k.Dict({'a': 2, 'b': 3, 'c': 5})  # is also available

        a: k.Optional[int] = dictionary['a']  # Optional(2)
        dictionary['d'] = 7
        count: int = dictionary.count  # 4

        for key, value in dictionary:
            print("%s -> %d" % (key, value))

        self.assertEqual(a, k.some(2))
        self.assertEqual(count, 4)
