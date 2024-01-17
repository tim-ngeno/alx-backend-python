#!/usr/bin/env python3
"""write a regular function to return a asyncio.Task object"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[None]:
    """
    Returns an asyncio.Task object for the wait_random coroutine

    Args:
        max_delay (int): The maximum value of the wait time in seconds

    Returns:
        asyncio.Task: an asyncio task object representing the execution
        of wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
