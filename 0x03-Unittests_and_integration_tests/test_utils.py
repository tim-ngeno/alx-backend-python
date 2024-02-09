#!/usr/bin/env python3
""" Parameterize a unit test """

from parameterized import parameterized
from typing import Any, Dict, Tuple, Type, Union
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
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
    def test_access_nested_map(
            self, nested_map: Dict[str, Any], path: Tuple[str, ...],
            expected_result: Any) -> None:
        """
        Tests that access_nested_map returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)

    @parameterized.expand([
        ({}, ('a', ), KeyError),
        ({'a': 1}, ('a', 'b'), (1, KeyError))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict[str, Any], path: Tuple[str, ...],
            expected_exception: Union[Type[Exception],
                                      Tuple[Any, Type[Exception]]]
    ) -> None:
        """
        Tests that a keyerror is raised for non-existent or incorrect keys
        """
        with self.assertRaises(expected_exception=KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    A unit test for the implementation of utils.get_json function
    """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Tests that the utils.get_json method returns the expected result
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    """
    A sample test class
    """

    def a_method(self):
        """ a method that returns an int value """
        return 42

    @memoize
    def a_property(self):
        """ returns a call to a_method """
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """
    Unittest class for utils.memoize
    """
    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test that calling a_property twice returns the correct result
        and a_method is only called once
        """
        test_instance = TestClass()
        mock_a_method.return_value = 42

        # Call a_property twice, assert the correct answer is returned
        res_1 = test_instance.a_property
        res_2 = test_instance.a_property

        self.assertEqual(res_1, 42)
        self.assertEqual(res_2, 42)

        # Assert that a_method is only called once
        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
