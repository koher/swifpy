from .context import swifpy as k
import unittest


class TestArray(unittest.TestCase):
    def test_sample(self):
        numbers: k.Array[int] = k.list(2, 3, 5)

        second: int = numbers[1]    # 3
        count: int = numbers.count  # 3

        squared: k.Array[int] = numbers.map(lambda x: x * x)            # [4, 9, 25]
        odd: k.Array[int] = numbers.filter(lambda x: x % 2 != 0)        # [3, 5]
        sum: k.Array[int] = numbers.reduce(0, lambda r, x: r + x)       # 10
        twice: k.Array[int] = numbers.flat_map(lambda x: k.list(x, x))  # [2, 2, 3, 3, 5, 5]

        first: k.Optional[int] = numbers.first  # Optional(2)
        third: k.Optional[int] = numbers.last   # Optional(5)

        for number in numbers:
            print(number)

        self.assertEqual(second, 3)
        self.assertEqual(count, 3)

        self.assertEqual(squared, k.list(4, 9, 25))
        self.assertEqual(odd, k.list(3, 5))
        self.assertEqual(sum, 10)
        self.assertEqual(twice, k.list(2, 2, 3, 3, 5, 5))

        self.assertEqual(first, k.some(2))
        self.assertEqual(third, k.some(5))
