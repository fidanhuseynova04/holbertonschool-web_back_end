#!/usr/bin/env python3
"""
Module that contains sum_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Function return sum of elements of the list
    '''
    return sum(mxd_lst)
