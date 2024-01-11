#!/usr/bin/env python3
"""
Write a type-annotated function sum_list which takes a list
`input_list`(list of floats) as an argument and returns their sum as a
float
"""


def sum_list(input_list: list[float]) -> float:
    """
    Takes an input list of floating point numbers and returns their sum
    as a floating point number
    """
    return sum(input_list)
