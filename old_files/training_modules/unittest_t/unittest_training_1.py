import unittest

# Function for test
def add_numbers(x,y,z):
    if type(x) not in [int, float]:
        raise TypeError('Not number')
    if type(y) not in [int, float]:
        raise TypeError('Not number')
    if type(z) not in [int, float]:
        raise TypeError('Not number')
    if x < 0 or y < 0 or z < 0:
        raise ValueError('Less than zero')
    return x+y+z
# -----------------

class TestAddNumbers(unittest.TestCase):

    def test_area(self):
        self.assertEqual(add_numbers(10,20,30), 60)
        self.assertEqual(add_numbers(10,20,5), 35)
        self.assertEqual(add_numbers(0,0,0), 0)
        self.assertEqual(add_numbers(10,30,30), 70)

    def test_values(self):
        self.assertRaises(ValueError, add_numbers, -5, -10, -20)
        self.assertRaises(ValueError, add_numbers, -1, -7, 1)

    def test_types(self):
        self.assertRaises(TypeError, add_numbers, 5+2j)
        self.assertRaises(TypeError, add_numbers, 'five')
        self.assertRaises(TypeError, add_numbers, [23,34])
        self.assertRaises(TypeError, add_numbers, [22])
        self.assertRaises(TypeError, add_numbers, True)