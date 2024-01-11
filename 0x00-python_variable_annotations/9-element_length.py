#!/usr/bin/env python3
"""
Annotate a  function using duck type and return values with the
approprirate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the item and its length
    """
    return [(i, len(i)) for i in lst]
