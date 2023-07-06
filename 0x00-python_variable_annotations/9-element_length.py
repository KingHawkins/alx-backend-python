#!/usr/bin/env python3
"""
9-element.py
"""
from typing import List, Sequence, Tuple, Any, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotation.
    """
    return [(i, len(i)) for i in lst]
