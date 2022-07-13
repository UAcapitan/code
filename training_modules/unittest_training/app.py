import unittest
from parameterized import parameterized

def calculator(e):
    if len(e) != 3:
        raise ValueError('Incorrect data')
    try:
        a, sym, b = int(e[0]), e[1], int(e[2])
    except ValueError:
        raise ValueError('Incorrect type of data')
    if sym == '+':
        return a + b
    elif sym == '-':
        return a - b
    elif sym == '*':
        return a * b
    elif sym == '/':
        return a / b
    else:
        raise ValueError('Incorrect symbol')

class Tests(unittest.TestCase):
    @parameterized.expand([
        [[1, "+", 2], 3],
        [[1, "*", 10], 10],
        [[7, "-", 4], 3],
        [[9, "/", 3], 3.0]
    ])
    def test_calculator(self, a, b):
        self.assertEqual(calculator(a), b)

    def test_raise_value(self):
        with self.assertRaises(ValueError) as e:
            calculator('text')
    
    def test_raise_type(self):
        with self.assertRaises(TypeError) as e:
            calculator('text', '')

if __name__ == "__main__":
    unittest.main() #pragma: no cover