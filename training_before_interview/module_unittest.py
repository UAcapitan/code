import unittest

def tested_function():
    pass

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(tested_function('Hello world'), 'World hello')
        self.assertEqual(tested_function('I love you'), 'You love I')
        self.assertEqual(tested_function('Word'), 'Word')
    
    def test2(self):
        with self.assertRaises(Exception) as context:
            tested_function()

        self.assertTrue('Empty field error' in context.exception)

        with self.assertRaises(Exception) as context:
            tested_function([])

        self.assertTrue('Empty field error' in context.exception)

        with self.assertRaises(Exception) as context:
            tested_function('')

        self.assertTrue('Empty field error' in context.exception)

    def test2(self):
        with self.assertRaises(Exception) as context:
            tested_function(42)

        self.assertTrue('Type of field error' in context.exception)

        with self.assertRaises(Exception) as context:
            tested_function(0.7)

        self.assertTrue('Type of field error' in context.exception)

        with self.assertRaises(Exception) as context:
            tested_function({'1': 'test'})

        self.assertTrue('Type of field error' in context.exception)




if __name__ == "__main__":
    unittest.main()