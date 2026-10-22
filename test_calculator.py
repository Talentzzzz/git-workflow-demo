import unittest

from calculator import add, divide, subtract


class CalculatorTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self) -> None:
        self.assertEqual(divide(6, 3), 2)

    def test_divide_floats(self) -> None:
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

    def test_divide_negative(self) -> None:
        self.assertEqual(divide(-9, 3), -3)

    def test_divide_by_zero(self) -> None:
        with self.assertRaisesRegex(ValueError, "b must not be zero"):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
