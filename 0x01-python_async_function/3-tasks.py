#!/usr/bin/env python3
"""write a regular function to return a asyncio.Task object"""


def task_wait_random(max_delay: int):
    """
    Returns an asyncio.Task object
    """
    async def async_coroutine():
        pass
    return asyncio.create_task(async_coroutine())
