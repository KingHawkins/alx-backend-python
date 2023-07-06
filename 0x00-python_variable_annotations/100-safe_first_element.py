#!/usr/bin/env python3
"""
10-main.py
"""
from typing import Any, Union, Sequence
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
