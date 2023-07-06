#!/usr/bin/env python3
"""
101-main.
"""
from types import NoneType
from typing import Union, TypeVar, Mapping, Any


T: TypeVar = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, NoneType]) -> Union[Any, T]:
    """
    Implementation.
    """
    if key in dct:
        return dct[key]
    else:
        return default
