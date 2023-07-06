#!/usr/bin/env python3
"""
6-sum_mixed_types.py
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns sum of items in the list.
    """
    value: float = 0
    for item in mxd_lst:
        value = value + item
    return value
