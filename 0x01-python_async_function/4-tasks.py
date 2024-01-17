#!/usr/bin/env python3
""" Alter the coroutine `wait_n` from task 1 """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay

    Args:
        n (int): The number of times to spawn wait_random
        max_delay (int): Maximum value of the wait time in seconds
    """
    delays = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
