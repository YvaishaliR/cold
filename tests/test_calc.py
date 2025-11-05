import unittest
from calc import add, subtract, multiply

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertRaises(ValueError, add, -1, 2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertRaises(ValueError, subtract, 5, -3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 2), 8)
        self.assertRaises(ValueError, multiply, -2, 4)

if __name__ == "__main__":
    unittest.main() 
