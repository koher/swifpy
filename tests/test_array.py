from swifpy import Array, Optional
import unittest


class TestArray(unittest.TestCase):
    def test_sample(self):
        numbers: Array[int] = Array([2, 3, 5])

        second: int = numbers[1]    # 3
        count: int = numbers.count  # 3

        squared: Array[int] = numbers.map(lambda x: x * x)            # [4, 9, 25]
        odd: Array[int] = numbers.filter(lambda x: x % 2 != 0)        # [3, 5]
        sum: Array[int] = numbers.reduce(0, lambda r, x: r + x)       # 10
        twice: Array[int] = numbers.flat_map(lambda x: Array([x, x]))  # [2, 2, 3, 3, 5, 5]

        first: Optional[int] = numbers.first  # Optional(2)
        third: Optional[int] = numbers.last   # Optional(5)

        for number in numbers:
            print(number)

        self.assertEqual(second, 3)
        self.assertEqual(count, 3)

        self.assertEqual(squared, Array([4, 9, 25]))
        self.assertEqual(odd, Array([3, 5]))
        self.assertEqual(sum, 10)
        self.assertEqual(twice, Array([2, 2, 3, 3, 5, 5]))

        self.assertEqual(first, Optional(2))
        self.assertEqual(third, Optional(5))
