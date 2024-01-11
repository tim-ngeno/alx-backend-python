#!/usr/bin/env python3
"""
Write a type annotated function make_multiplier that takes a float
`multiplier` and returns a function that multiplies a float by
multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the give multiplier

    Args:
        multiplier (float): the value by which the input will be
        multiplied

    Returns:
        Callable[[float], float]: A function that takes a float as input
    and returns the product from the multiplication
    """
    def multiply_function(x: float) -> float:
        """
        Returns the result of the multiplication between the float and
        multiplier
        """
        return x * multiplier

    return multiply_function
