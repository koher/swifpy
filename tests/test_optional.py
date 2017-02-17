from swifpy import Int, Nil, Optional, Some, NilError
import unittest


class TestOptional(unittest.TestCase):
    def test_sample(self):
        a: Optional[Int] = Some(2)
        b: Optional[Int] = Some(3)
        n: Optional[Int] = Nil

        if a:
            print('Reaches here.')

        if not n:
            print('Reaches here.')

        squared1: Optional[Int] = a.map(lambda x: x * x)                    # Optional(4)
        squared2: Optional[Int] = n.map(lambda x: x * x)                    # Nil
        sum1: Optional[Int] = a.flat_map(lambda x: b.map(lambda y: x + y))  # Optional(5)
        sum2: Optional[Int] = a.flat_map(lambda x: n.map(lambda y: x + y))  # Nil

        unwrapped: Int = a.x  # `!` in Swift: `x` of e*x*clamation marks
        try:
            _ = n.x  # NilError
            self.fail('Never reaches here.')
        except NilError:
            print('Reaches here.')

        # `??` in Swift: `q` of *q*uestion marks
        coalesced1: Int = a.qq(0)  ## 2
        coalesced2: Int = n.qq(0)  ## 0

        self.assertEqual(squared1, Some(4))
        self.assertEqual(squared2, Nil)
        self.assertEqual(sum1, Some(5))
        self.assertEqual(sum2, Nil)
        self.assertEqual(unwrapped, 2)
        self.assertEqual(coalesced1, 2)
        self.assertEqual(coalesced2, 0)
