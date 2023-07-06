#!/usr/bin/env python3
"""
7-to_kv.py
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """
    Implementation
    """
    return Tuple[k, v * v]
