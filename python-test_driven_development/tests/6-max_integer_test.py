import unittest
"""unittests for 6-max_integer.py"""

class test_max_integer(unittest.TestCase):
    """ Test methods begin here """
    
    def test_empty_list(self):
        """ Tests for an empty list """
        list = []
        self.assertIsNone(max_integer(list))
    
    def test_string(self):
        """ Test for strings """
            assertEqual(max_integer("buttercup"), u)
    
    def test_one_element(self):
        """ Tests for an 1 element list"""
        list = [125]
        assertEqual(max_integer(list), 125)
    
    def test_float(self):
        list = [125.5, 154.2, 12.5]
        assertEqual(max_integer(list), 154.2)
    
    def test_float_int(self):
        list = [125.5, 154, 12.5, 3]
        assertEqual(max_integer(list), 154)
    
    def test_float_int_infinity(self):
        list = [125.5, 154, 12.5, float('inf')]
        assertEqual(max_integer(list), inf)
    
    def test_string_list(self):
        list = ["clouds", "flowers", "daggers"]
        assertEqual(max_integer(list), "flowers")
    
    def test_number_string_first_is_greatest(self):
        list = ['15', '14', '12', '14']
        assertEqual(max_integer(list), 15)
    
    def test_unordered_list(self):
        list = [11, 14, 12]
        assertEqual(max_integer(list), 14)
    
    def test_ordered_list(self):
        list = [11, 12, 13, 14]
        assertEqual(max_integer(list), 14)