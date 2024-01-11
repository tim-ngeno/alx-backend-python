#!/usr/bin/env python3
"""
Write a type-annotated function `floor` which takes a float `n` as
an argument and returns the floor of the float as a result
"""

import math


def floor(n: float) -> int:
    """
    Floors a floating point number and returns the result

    Args:
        n (float): floating point argument to be floored
    """
    return math.floor(n)
