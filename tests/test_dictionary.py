from swifpy import Dictionary, Int, Optional, Some, String
import unittest


class TestDictionary(unittest.TestCase):
    def test_sample(self):
        dictionary: Dictionary[String, Int] = Dictionary({'a': 2, 'b': 3, 'c': 5})

        a: Optional[Int] = dictionary['a']  # Optional(2)
        dictionary['d'] = 7
        count: Int = dictionary.count  # 4

        for key, value in dictionary:
            print("%s -> %d" % (key, value))

        self.assertEqual(a, Some(2))
        self.assertEqual(count, 4)
