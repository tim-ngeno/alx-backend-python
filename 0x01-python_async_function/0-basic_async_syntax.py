#!/usr/bin/env python3
"""An asynchronous coroutine that generates a random delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay before returning
    the delay value

    Args:
        max_delay (int): The maximum value of the wait time in seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
