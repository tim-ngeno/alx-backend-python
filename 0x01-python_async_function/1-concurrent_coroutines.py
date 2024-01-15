#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay

    Args:
        n (int): The number of times to spawn wait_random
        max_delay (int): Maximum value of the wait time in seconds
    """
    delays = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
