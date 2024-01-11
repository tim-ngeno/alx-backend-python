#!/usr/bin/env python3
"""
Using TypeVar to annotate functions and return values
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
                     None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Parameters:
        dct (Dict[K, V]): The dictionary to retrieve the value from
        key (K): the key to look up in the dictionary
        default (Optional[V]): The default value to return if key is not found

    Returns:
        V: The value  associated with the key, if found
    """
    if key in dct:
        return dct[key]
    else:
        return default
