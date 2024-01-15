#!/usr/bin/env python3
"""write a regular function to return a asyncio.Task object"""

import asyncio


def task_wait_random(max_delay: int):
    """
    Returns an asyncio.Task object
    """
    async def async_coroutine():
        await asyncio.sleep(1)
    return asyncio.create_task(async_coroutine())
