import unittest

def tested_function(string=''):
    if string:
        return ' '.join(string.lower().split()[::-1]).capitalize()
    else:
        raise Exception('Empty field error')

class Tests(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()