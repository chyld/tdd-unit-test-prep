from unittest import TestCase

from .. import simple as s


class TestSimple(TestCase):
    def test_add1(self):
        self.assertEqual(s.add1(3), 4)
        self.assertNotEqual(s.add1(3), 5)

    def test_square(self):
        self.assertEqual(s.square(3), 9)

    def test_is_even(self):
        self.assertFalse(s.is_even(3))
        self.assertTrue(s.is_even(2))

    def test_get_odds(self):
        nums = range(3, 20)
        odds = s.get_odds(nums)
        self.assertEqual(len(odds), 9)
        self.assertIn(5, odds)
        self.assertNotIn(6, odds)

    def test_only_natural_division(self):
        result = s.only_natural_divison(3, 4)
        self.assertAlmostEqual(result, 0.75, 2)
        with self.assertRaises(ValueError):
            s.only_natural_divison(3, -1)

    def test_dot_product(self):
        v1 = [1, 2]
        v2 = [3, 4]
        result = s.dot_product(v1, v2)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 11)
