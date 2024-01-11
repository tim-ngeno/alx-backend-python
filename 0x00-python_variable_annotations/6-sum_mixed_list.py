#!/usr/bin/env python3
"""
Write a type-annotated function which takes a list `mxd_lst` of integers
and floats and returns their sum as float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and returns their sum as a float

    Args:
        mxd_lst (list): input list of integers
    """
    return float(sum(mxd_lst))
