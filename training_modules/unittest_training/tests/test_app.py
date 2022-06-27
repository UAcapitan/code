import unittest
from unittest import TestCase
import sys
sys.path.insert(1, '/home/ed/Desktop/EdMix/code/training_modules/unittest_training')
from app import calculator

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator([22, '+', 2]), 24)
        self.assertEqual(calculator([29, '+', 9]), 38)
        self.assertEqual(calculator([15, '+', 2]), 17)

    def test_minus(self):
        self.assertEqual(calculator([22, '-', 2]), 20)
        self.assertEqual(calculator([20, '-', 1]), 19)
        self.assertEqual(calculator([10, '-', 3]), 7)

    def test_multiply(self):
        self.assertEqual(calculator([22, '*', 2]), 44)
        self.assertEqual(calculator([20, '*', 1]), 20)
        self.assertEqual(calculator([10, '*', 3]), 30)

    def test_divide(self):
        self.assertEqual(calculator([22, '/', 2]), 11.0)
        self.assertEqual(calculator([20, '/', 1]), 20.0)
        self.assertEqual(calculator([9, '/', 3]), 3.0)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('just a test')
        self.assertEqual('Incorrect data', e.exception.args[0])

if __name__ == '__main__':
    unittest.main()