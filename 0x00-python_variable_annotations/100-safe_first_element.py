#!/usr/bin/env python3
"""
10-main.
"""
from typing import Any, Union, Sequence
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Implementation.
    """
    if lst:
        return lst[0]
    else:
        return NoneType
