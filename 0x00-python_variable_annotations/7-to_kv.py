#!/usr/bin/env python3
"""
Write a type-annotated function `to_kv` that takes a string `k` and an
int or float `v` as arguments and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple formed by the arguments k and v

    Args:
        k (str): string argument
        v (int|float): an argument that can either be a float or int
    """
    v = v ** 2
    return (k, v)
