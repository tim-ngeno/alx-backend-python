---

# Asynchronous I/O with Python asyncio

## Table of Contents
1. [Introduction](#introduction)
2. [Async and Await Syntax](#async-and-await-syntax)
3. [Executing an Async Program with asyncio](#executing-an-async-program-with-asyncio)
4. [Running Concurrent Coroutines](#running-concurrent-coroutines)
5. [Creating asyncio Tasks](#creating-asyncio-tasks)
6. [Using the Random Module with asyncio](#using-the-random-module-with-asyncio)


## Introduction

Asynchronous I/O (input/output) allows you to perform non-blocking operations, enabling efficient multitasking and concurrent execution of code. Python's asyncio module provides a framework for working with asynchronous code.

This README aims to explain the fundamental concepts of asynchronous programming in Python using asyncio, including syntax, program execution, concurrent coroutines, task creation, and integration with the random module.

## Async and Await Syntax

In Python, the `async` and `await` keywords are used to define asynchronous functions and await asynchronous calls, respectively. An asynchronous function is a coroutine, which can be paused and resumed, allowing other tasks to run in the meantime.

```python
import asyncio

async def example_coroutine():
    print("Start Coroutine")
    await asyncio.sleep(1)
    print("End Coroutine")

# Running the coroutine
asyncio.run(example_coroutine())
```

## Executing an Async Program with asyncio

To execute an asynchronous program, use the `asyncio.run()` function. It sets up the event loop, runs the provided coroutine, and closes the loop afterward.

```python
import asyncio

async def main():
    # Your asynchronous code here

if __name__ == "__main__":
    asyncio.run(main())
```

## Running Concurrent Coroutines

To run multiple coroutines concurrently, use `asyncio.gather()` or `asyncio.create_task()`.

```python
import asyncio

async def coroutine1():
    # Your code here

async def coroutine2():
    # Your code here

async def main():
    await asyncio.gather(coroutine1(), coroutine2())
    # OR
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    await asyncio.gather(task1, task2)
```

## Creating asyncio Tasks

Tasks are used to schedule and manage the execution of coroutines. They can be awaited or run concurrently.

```python
import asyncio

async def example_task():
    # Your code here

async def main():
    task = asyncio.create_task(example_task())
    await task
```

## Using the Random Module with asyncio

When working with asynchronous code, the random module needs special consideration. The `random` module is not coroutine-friendly, so use `asyncio.to_thread()` to run synchronous code in a separate thread.

```python
import asyncio
import random

async def async_random():
    # Using random module asynchronously
    return await asyncio.to_thread(random.randint, 1, 10)

async def main():
    result = await async_random()
    print(f"Async Random Result: {result}")

```
