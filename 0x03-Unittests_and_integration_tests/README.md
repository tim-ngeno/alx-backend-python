# Unit Testing and Integration Testing with unittest in Python

## Overview

This GitHub repository provides a comprehensive guide on using `unittest`, the built-in unit testing framework in Python, along with `unittest.mock`, a powerful mock object library. It covers various aspects of unit testing, including mocking readonly properties, parameterized tests, and memoization.

## Table of Contents
- [Getting Started](#getting-started)
- [Unit Testing with unittest](#unit-testing-with-unittest)
  - [Basic Test Structure](#basic-test-structure)
  - [Assertions](#assertions)
- [Mocking with unittest.mock](#mocking-with-unittestmock)
  - [Mocking Readonly Properties](#mocking-readonly-properties)
  - [Example: Mocking a Readonly Property](#example-mocking-a-readonly-property)
- [Parameterized Tests](#parameterized-tests)
  - [Example: Parameterized Test](#example-parameterized-test)
- [Memoization](#memoization)
  - [Example: Memoization in Unit Tests](#example-memoization-in-unit-tests)

## Getting Started

Clone this repository to get started with unit and integration testing in Python.

```bash
git clone https://github.com/your_username/your_project.git
cd your_project
```

## Unit Testing with unittest

### Basic Test Structure

`unittest` follows a simple structure for writing test cases. Create a test class that inherits from `unittest.TestCase` and define test methods starting with the word "test."

```python
import unittest

class MyTests(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)
```

### Assertions

`unittest` provides various assertion methods to check for expected outcomes. Some common assertions include `assertTrue`, `assertFalse`, `assertEqual`, and more.

```python
class TestAssertions(unittest.TestCase):
    def test_assert_true(self):
        self.assertTrue(2 + 2 == 4)

    def test_assert_false(self):
        self.assertFalse(2 + 2 == 5)

    def test_assert_equal(self):
        self.assertEqual(len([1, 2, 3]), 3)
```

## Mocking with unittest.mock

### Mocking Readonly Properties

`unittest.mock` allows you to create mock objects and replace attributes, including readonly properties.

To mock a readonly property, use the `@property` decorator in the mock class.

```python
from unittest.mock import Mock

class MyClass:
    @property
    def readonly_property(self):
        return 42

# Mocking readonly property
mocked_instance = Mock(spec=MyClass)
mocked_instance.readonly_property = 99

# Accessing the mocked property
print(mocked_instance.readonly_property)  # Output: 99
```

### Example: Mocking a Readonly Property

```python
from unittest import TestCase, mock

class MyTests(TestCase):
    def test_mock_readonly_property(self):
        with mock.patch('path.to.MyClass.readonly_property', new_callable=mock.PropertyMock) as mock_property:
            mock_property.return_value = 99

            instance = MyClass()
            result = instance.readonly_property

        self.assertEqual(result, 99)
```

## Parameterized Tests

`unittest` supports parameterized tests using the `@unittest.expectedFailure` decorator.

```python
from unittest import TestCase, main
from parameterized import parameterized

class MyTests(TestCase):
    @parameterized.expand([
        (1, 2, 3),
        (4, 5, 9),
        (10, 20, 30),
    ])
    def test_addition(self, a, b, expected_sum):
        result = a + b
        self.assertEqual(result, expected_sum)

if __name__ == '__main__':
    main()
```

### Example: Parameterized Test

Install the `parameterized` package to enable parameterized testing.

```bash
pip install parameterized
```

## Memoization

Memoization is a technique to cache the results of expensive function calls and return the cached result when the same inputs occur again.

### Example: Memoization in Unit Tests

```python
from unittest import TestCase, main
from functools import lru_cache

class MyTests(TestCase):
    @lru_cache(maxsize=None)
    def expensive_function(self, n):
        # Expensive computation
        return n * n

    def test_memoization(self):
        result1 = self.expensive_function(5)
        result2 = self.expensive_function(5)

        self.assertEqual(result1, result2)

if __name__ == '__main__':
    main()
```

## Conclusion

This repository provides a comprehensive guide to unit and integration testing in Python using `unittest` and `unittest.mock`. Feel free to explore the examples and adapt them to your project's needs. Happy testing!
