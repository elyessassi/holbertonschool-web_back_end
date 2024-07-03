#!/usr/bin/env python3
"""
a type-annotated function floor which takes a float n as argument and
 returns the floor of the floa
"""


def floor(n: float) -> int:
    """The function"""
    return int(n) if n >= 0 else (int(n) - 1)
