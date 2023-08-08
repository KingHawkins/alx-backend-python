#!/usr/bin/env python3
"""
Asynchronous corotine that takes in an integer.
"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    Implementation.
    """
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
