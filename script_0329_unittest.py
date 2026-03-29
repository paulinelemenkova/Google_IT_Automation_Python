#import os
#os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
#os.getcwd()

#!/bin/env/python3

import unittest

# The function we want to test
def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add_integers(self):
        # We 'assert' that 2 + 3 should equal 5
        self.assertEqual(add(2, 3), 5)

    def test_add_strings(self):
        # We 'assert' that 'a' + 'b' should equal 'ab'
        self.assertEqual(add('a', 'b'), 'ab')

if __name__ == '__main__':
    unittest.main()
