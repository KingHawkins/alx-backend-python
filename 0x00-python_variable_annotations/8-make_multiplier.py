#!/usr/bin/env python3
"""
8-make_multiplier.py
"""
from typing import Callable


def multiply(integer: float) -> float:
    return integer * integer


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    """
    return multiply
