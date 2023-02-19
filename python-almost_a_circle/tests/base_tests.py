#!/usr/bin/pthon3
"""==========================
Tests for "base.py"
==========================

--------------------------"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Base_instantiation(unittest.TestCase):
    """ Tests for the instantiation of the Base class"""

    def id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def float_id(self):
        self.assertEqual(3.5, Base(3.5).id)

    def str_id(self):
        self.assertEqual("Something", Base("Something").id)

    def bool_id(self):
        self.assertEqual(True, Base(True).id)

    def inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

class Test_Base_to_json_string(unittest.TestCase):
    """ Test for JSON methods """

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def json_string_type_rectangle(self):
        r = Rectangle(1, 5, 10, 12, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        s = Square(5, 7, 9, 3)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

class Test_Base_save_to_file(unittest.TestCase):
    """ Tests for save_to_file method """

    @classmethod
    def cleanup(self):
        """ Deletes temp files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def save_rectangle(self):
        r = Rectangle(5, 3, 2, 4, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def save_square(self):
        r = Square(3, 2, 4, 8)
        Square.save_to_file([r])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
    

if __name__ == "__main__":
    unittest.main()
