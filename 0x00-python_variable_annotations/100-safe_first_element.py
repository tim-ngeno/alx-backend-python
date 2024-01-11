#!/usr/bin/env python3
"""
Augment a code block with the correct duck-typed annotatios for the
inputs whose values are unknown
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first argument of the sequence lst if it exists,
    otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
