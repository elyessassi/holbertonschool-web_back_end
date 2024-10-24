#!/usr/bin/env python3
"""Test file for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """Class to test utils.access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), (1)),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), (2))
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """  Method that tests the
          test_access_nested_map method
          if method is correct  """
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


class TestGetJson(unittest.TestCase):
    """Class to test utils.get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, url, payload, mocked_get_request):
        mocked_get_request.json.return_value = payload
        get_json(url)
        mocked_get_request.assert_called_once_with(url)
        self.assertEqual(mocked_get_request.json(), payload)


class TestMemoize(unittest.TestCase):
    """ class to test utils.memoize method"""
    def test_memoize(self):
        """Method to test the memoize method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mocked_a_method:
            x = TestClass()
            x.a_property
            x.a_property
            mocked_a_method.assert_called_once()
