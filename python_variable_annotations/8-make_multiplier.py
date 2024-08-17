#!/usr/bin/env python3
"""
Module that contains sum_list function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Declaration
    '''
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
