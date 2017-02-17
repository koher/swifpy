from swifpy import Array, Dictionary, Int, Optional, Some, String
import unittest


class TestSample(unittest.TestCase):
    def test_sample(self):
        array: Array[Int] = Array([2, 3, 5])
        squared: Array[Int] = array.map(lambda x: x * x)  # [4, 9, 25]
        count: Int = array.count  # 3

        dictionary: Dictionary[String, Int] = Dictionary({'a': 2, 'b': 3, 'c': 5})
        a: Optional[Int] = dictionary['a']  # Optional(2)
        b: Optional[Int] = dictionary['b']  # Optional(3)

        sum: Optional[Int] = a.flat_map(lambda x: b.map(lambda y: x + y))  # Optional(5)

        self.assertEqual(squared, Array([4, 9, 25]))
        self.assertEqual(count, 3)
        self.assertEqual(a, Some(2))
        self.assertEqual(b, Some(3))
        self.assertEqual(sum, Some(5))
