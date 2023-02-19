#!/usr/bin/python3
"""Tests for base.py"""
import unittest
from models.base import Base

class test_base(unittest.TestCase):
    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_save_id_passed(self):
        self.assertEqual(89, Base(89).id)

    def test_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_from_json_string_base(self):
        list_input = [{"id": 89}]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

if __name__ == "__main__":
    unittest.main()
