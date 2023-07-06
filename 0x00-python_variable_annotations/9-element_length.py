#!/usr/bin/env python3
"""
9-element.py
"""
from collections.abc import Iterable
from typing import List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """
    Annotation.
    """
    return Tuple[(i, len(i)) for i in lst]
