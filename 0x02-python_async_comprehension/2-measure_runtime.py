#!/usr/bin/env python3
""" Write a coroutine to execute a function four times in parallel """

import asyncio
import time

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for an async comprehension run 4 times in
    parallel using asyncio.gather
    """
    start = time.time()
    await asyncio.gather(
        async_comp(), async_comp(), async_comp(), async_comp()
    )
    end = time.time()
    return end - start
