#!/usr/bin/env python3
"""
Measure the runtime values of asynchronous function calls
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns total_time / n as a float

    Args:
        n (int): Number of times to spawn wait_n
        max_delay (int): Maximum value of the wait time in seconds
    """
    async def run_measure_time():
        """Runs the outer function measure_time asynchronously"""
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()

        total_time = end_time - start_time
        return total_time / n

    return asyncio.run(run_measure_time())
