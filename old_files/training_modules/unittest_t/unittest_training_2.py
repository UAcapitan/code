import unittest

# Function for test
def writeNumber(x):
    if type(x) not in [int]:
        raise TypeError('Wrong type of number')
    if x <= 1:
        raise ValueError('Number less than 1')
    return x
# -----------------

class TestWriteNumber(unittest.TestCase):

    def test_area(self):
        self.assertEqual(writeNumber(9), 9)
        self.assertEqual(writeNumber(2), 2)
        self.assertEqual(writeNumber(5), 5)
        self.assertEqual(writeNumber(3), 3)
        self.assertEqual(writeNumber(7), 7)

    def test_values(self):
        self.assertRaises(ValueError, writeNumber, -1)
        self.assertRaises(ValueError, writeNumber, 0)
        self.assertRaises(ValueError, writeNumber, 1)

    def test_types(self):
        self.assertRaises(TypeError, writeNumber, True)
        self.assertRaises(TypeError, writeNumber, '5')
        self.assertRaises(TypeError, writeNumber, [1,2,3])
        self.assertRaises(TypeError, writeNumber, [1])
        self.assertRaises(TypeError, writeNumber, (1,2,3))
        self.assertRaises(TypeError, writeNumber, {'1':'1'})
        self.assertRaises(TypeError, writeNumber, {1,2,3})
        self.assertRaises(TypeError, writeNumber, 7.5)