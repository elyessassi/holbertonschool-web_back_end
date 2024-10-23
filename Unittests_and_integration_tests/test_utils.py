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
        """Method that tests the
          test_access_nested_map method  """
        self.assertEqual(access_nested_map(nested_map, path), expected)
