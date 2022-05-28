#!/usr/bin/env python3
"""Adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Retur array"""
    if len(arr1) != len(arr2):
        return None
    return [sum(pair) for pair in zip(arr1, arr2)]
