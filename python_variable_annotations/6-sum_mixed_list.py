#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes
 a list mxd_lst of integers and floats and returns their sum as a float
"""


from typing import List


def sum_mixed_list(input_list: List[float | int]) -> float:
    """the function"""
    x: float = 0
    for i in input_list:
        x += i
    return (x)
