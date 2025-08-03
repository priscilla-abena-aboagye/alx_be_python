import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self): 
        self.assertEqual(self.calc.add(10, 3), 13)
        self.assertEqual(self.calc.add(5, -2), 3)
        self.assertEqual(self.calc.add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_multiply(self): 
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(10, 0))
