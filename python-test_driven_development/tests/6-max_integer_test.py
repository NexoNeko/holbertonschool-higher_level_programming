# ==========================
# Tests for ``6-max_integer.py``
# ==========================

# --------------------------
"""unittests for 6-max_integer.py"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    """ defines unittest class for max_integer"""
    
    def test_empty_list(self):
        """ Tests for an empty list """
        list = []
        self.assertIsNone(max_integer(list))
    
    def test_string(self):
        """ Test for strings """
        self.assertEqual(max_integer("buttercup"), u)
    
    def test_one_element(self):
        """ Tests for an 1 element list"""
        list = [125]
        self.assertEqual(max_integer(list), 125)
    
    def test_float(self):
        """ Test for floats """
        list = [125.5, 154.2, 12.5]
        self.assertEqual(max_integer(list), 154.2)
    
    def test_float_int(self):
        """ Test for mixed float and int """
        list = [125.5, 154, 12.5, 3]
        self.assertEqual(max_integer(list), 154)
    
    def test_float_int_infinity(self):
        """ Test for float, int and infinity """
        list = [125.5, 154, 12.5, float('inf')]
        self.assertEqual(max_integer(list), inf)
    
    def test_string_list(self):
        """ Test for a list of strings """
        list = ["clouds", "flowers", "daggers"]
        self.assertEqual(max_integer(list), "flowers")
    
    def test_number_string_first_is_greatest(self):
        """ Test for a list of strings containing numbers """
        list = ['15', '14', '12', '14']
        self.assertEqual(max_integer(list), 15)
    
    def test_unordered_list(self):
        """ Test for an unordered list """
        list = [11, 14, 12]
        self.assertEqual(max_integer(list), 14)
    
    def test_ordered_list(self):
        """ Test for an ordered list """
        list = [11, 12, 13, 14]
        self.assertEqual(max_integer(list), 14)

if __name__ == '__main__':
    unittest.main()