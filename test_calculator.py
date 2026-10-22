import unittest

from calculator import add, divide, subtract


class CalculatorTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self) -> None:
        self.assertEqual(divide(6, 3), 2)


if __name__ == "__main__":
    unittest.main()
