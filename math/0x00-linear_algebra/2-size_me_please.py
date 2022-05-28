#!/usr/bin/env python3
"""Calculate the shape of a matrix"""


def matrix_shape(matrix):
    """Return the shape of matrix"""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])
