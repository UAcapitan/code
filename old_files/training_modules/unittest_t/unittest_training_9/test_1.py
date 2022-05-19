import unittest

# Functions for testing
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def sqrt(a):
    return a**0.5

def pow(a, b):
    return a**b
# ---------------------

class CalcBasicTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(4, 2), 2)

    def test_mul(self):
        self.assertEqual(mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(div(8, 4), 2)

class CalcExTests(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(pow(3, 3), 27)




