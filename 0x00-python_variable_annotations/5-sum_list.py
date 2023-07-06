#!/usr/bin/env python3
"""
5-sum_list.py
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of list items.
    """
    add: float = 0
    for item in input_list:
        add = add + item
    return add
