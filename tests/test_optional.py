from .context import kollect as k
import unittest

class TestOptional(unittest.TestCase):
    def test_sample(self):
        a: k.Optional[int] = k.some(2)
        b: k.Optional[int] = k.some(3)
        n: k.Optional[int] = k.none()

        if a:
            print('Reaches here.')

        if not n:
            print('Reaches here.')

        squared1: k.Optional[int] = a.map(lambda x: x * x)                    # Optional(4)
        squared2: k.Optional[int] = n.map(lambda x: x * x)                    # Optional()
        sum1: k.Optional[int] = a.flat_map(lambda x: b.map(lambda y: x + y))  # Optional(5)
        sum2: k.Optional[int] = a.flat_map(lambda x: n.map(lambda y: x + y))  # Optional()

        unwrapped = a.unwrapped
        try:
            _ = n.unwrapped  # UnwrappingError
            self.fail('Never reaches here.')
        except k.UnwrappingError:
            print('Reaches here.')

        self.assertEqual(squared1, k.some(4))
        self.assertEqual(squared2, k.none())
        self.assertEqual(sum1, k.some(5))
        self.assertEqual(sum2, k.none())
        self.assertEqual(unwrapped, 2)
