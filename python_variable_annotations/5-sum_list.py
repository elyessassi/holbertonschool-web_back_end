#!/usr/bin/env python3
"""
type-annotated function that takes a list of floats as argument and
 returns their sum as float
"""


def sum_list(input_list: list[float]) -> float:
    """the function"""
    return sum(input_list)
