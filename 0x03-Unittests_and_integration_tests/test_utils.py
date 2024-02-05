#!/usr/bin/env python3
""" Parameterize a unit test """

from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittest class for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Tests that access_nested_map returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)


if __name__ == "__main__":
    unittest.main()
