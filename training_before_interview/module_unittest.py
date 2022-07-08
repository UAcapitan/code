import unittest

def tested_function():
    pass

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(tested_function('Hello world'), 'World hello')
        self.assertEqual(tested_function('I love you'), 'You love I')
        self.assertEqual(tested_function('Word'), 'Word')

if __name__ == "__main__":
    unittest.main()