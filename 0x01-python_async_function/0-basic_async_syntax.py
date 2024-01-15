#!/usr/bin/env python3
"""Write an asynchronous coroutine with the random module"""
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay before returning
    the delay value

    Args:
        max_delay (int): The maximum value of the wait time in seconds
    """
    return random.uniform(0, max_delay)
