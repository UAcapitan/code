from importlib.resources import path
import unittest
from unittest.mock import patch
from parameterized import parameterized

def test_function():
    return 'String'

def tested_function(string=''):
    if string == 'string':
        return test_function()
    elif string:
        return ' '.join(string.lower().split()[::-1]).capitalize()
    else:
        raise Exception('Empty field error')

class Tests(unittest.TestCase):

    n = None

    @classmethod
    def setUpClass(cls):
        cls.n = 5
        print('Started\n')

    def test1(self):
        self.assertEqual(tested_function('Hello world'), 'World hello')
        self.assertEqual(tested_function('I love you'), 'You love i')
        self.assertEqual(tested_function('Word'), 'Word')
    
    def test2(self):
        with self.assertRaises(Exception):
            tested_function()

        with self.assertRaises(Exception):
            tested_function([])

        with self.assertRaises(Exception):
            tested_function('')

    def test3(self):
        with self.assertRaises(Exception):
            tested_function(42)

        with self.assertRaises(Exception):
            tested_function(0.7)

        with self.assertRaises(Exception):
            tested_function({'1': 'test'})

    @parameterized.expand([
        ['My work', 'Work my'],
        ['Story love', 'Love story'],
        ['New history line', 'Line history new']
    ])
    def test4(self, a, b):
        self.assertEqual(tested_function(a), b)

    def test5(self):
        with patch("module_unittest.test_function") as context:
            context.return_value = 'Text'

            self.assertEqual(tested_function('string'), 'Text')

    @classmethod
    def tearDownClass(cls):
        del cls.n
        print('\n\nFinished')

if __name__ == "__main__":
    unittest.main(exit=False)