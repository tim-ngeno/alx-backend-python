---

# Python Type Annotations Guide

A comprehensive guide on leveraging Python type annotations for cleaner code and improved maintainability.

## Table of Contents

1. [Introduction](#introduction)
2. [Type Annotations in Python 3](#type-annotations-in-python-3)
3. [Specifying Function Signatures](#specifying-function-signatures)
4. [Variable Types](#variable-types)
5. [Duck Typing](#duck-typing)
6. [Validating Code with Mypy](#validating-code-with-mypy)

## Introduction

Python 3 introduced type annotations, a powerful feature enabling developers to specify the expected types of variables and function parameters. This enhances code readability, aids in catching potential errors early, and facilitates better collaboration within development teams.

## Type Annotations in Python 3

Type annotations allow you to provide hints to the interpreter about the types used in your code. This information is not enforced at runtime but can be utilized by static analysis tools.

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

In this example, `a` and `b` are expected to be integers, and the function is expected to return an integer.

## Specifying Function Signatures

Type annotations can be applied to function parameters and return values, providing a clear contract for how a function should be used.

```python
def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."
```

Here, `name` is expected to be a string, `age` an integer, and the function returns a string.

## Variable Types

Type annotations can also be used for variables, helping to document and clarify their intended types.

```python
my_variable: List[str] = ["apple", "banana", "cherry"]
```

This declares `my_variable` as a list of strings.

## Duck Typing

Python follows the principle of duck typing, which focuses on an object's behavior rather than its type. Type annotations respect this philosophy by allowing flexibility in the types used, promoting adaptability.

```python
def print_length(obj: Any) -> None:
    print(len(obj))
```

This function can accept any object as long as it supports the `len` function.

## Validating Code with Mypy

[Mypy](http://mypy-lang.org/) is a static type checker for Python that can analyze your code and catch type-related errors before runtime.

To install Mypy:

```bash
pip install mypy
```

To validate your code:

```bash
mypy your_code.py
```
---
