#!/usr/bin/env python3
"""
7-to_kv.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Implementation.
    """
    return (k, v * v)
