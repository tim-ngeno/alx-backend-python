#!/usr/bin/env python3
"""Async comprehension"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    Returns 10 random numbers from an async generator function
    """
    return [i async for i in async_generator()]
