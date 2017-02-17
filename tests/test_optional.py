from swifpy import Int, Optional, UnwrappingError
import unittest


class TestOptional(unittest.TestCase):
    def test_sample(self):
        a: Optional[Int] = Optional(2)
        b: Optional[Int] = Optional(3)
        n: Optional[Int] = Optional(None)

        if a:
            print('Reaches here.')

        if not n:
            print('Reaches here.')

        squared1: Optional[Int] = a.map(lambda x: x * x)                    # Optional(4)
        squared2: Optional[Int] = n.map(lambda x: x * x)                    # Optional()
        sum1: Optional[Int] = a.flat_map(lambda x: b.map(lambda y: x + y))  # Optional(5)
        sum2: Optional[Int] = a.flat_map(lambda x: n.map(lambda y: x + y))  # Optional()

        unwrapped = a.unwrapped
        try:
            _ = n.unwrapped  # UnwrappingError
            self.fail('Never reaches here.')
        except UnwrappingError:
            print('Reaches here.')

        self.assertEqual(squared1, Optional(4))
        self.assertEqual(squared2, Optional(None))
        self.assertEqual(sum1, Optional(5))
        self.assertEqual(sum2, Optional(None))
        self.assertEqual(unwrapped, 2)
