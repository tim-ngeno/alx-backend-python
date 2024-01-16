#!/usr/bin/env python3
""" Write a coroutine that loops 10 times and yields a random number """

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """
    Runs a loop 10 times, waiting 1 second each time, and yields a
    random number between 0 and 10
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
