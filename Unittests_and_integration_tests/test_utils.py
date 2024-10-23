#!/usr/bin/env python3
"""Test file for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class to test utils.py"""
    @parameterized.expand([
        ({"a": 1}, ("a",), (1)),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), (2))
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """  Method that tests the
          test_access_nested_map method  """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), (KeyError)),
        ({"a": 1}, ("a", "b"), (KeyError))
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Method that tests if  test_access_nested_map method
            raises a key error if the index is wrong """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
