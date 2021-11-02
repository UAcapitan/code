import unittest

# Functions for test

def sum_list_nums(x):
    return sum(x)

def reverse_words(words):
    w = words.lower()
    l = w.split()
    l.reverse()
    return ' '.join(l)

def min_index_in_list(l):
    return l.index(min(l))

# --------------------

class CalcTests(unittest.TestCase):
    
    def test_sum_list_nums(self):
        self.assertEqual(sum_list_nums([1,2,3]), 6)
        self.assertEqual(sum_list_nums([2,2,3]), 7)
        self.assertEqual(sum_list_nums([0,0,0]), 0)

    def test_reverse_words(self):
        self.assertEqual(reverse_words('Hello world'), 'world hello')
        self.assertEqual(reverse_words('My name is Kiril'), 'kiril is name my')
        self.assertEqual(reverse_words('My dear friend'), 'friend dear my')

class OtherCalcTests(unittest.TestCase):

    def test_min_index_in_list(self):
        self.assertEqual(min_index_in_list([5,1,3,6,9]), 1)
        self.assertEqual(min_index_in_list([8,4,2,4,0]), 4)
        self.assertEqual(min_index_in_list([91,24,55,17,34]), 3)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)