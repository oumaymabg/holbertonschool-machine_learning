#!/usr/bin/env python3
"""
Adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
  """
  add_matrices2D
  """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[x + y for x, y in zip(a, b)] for a, b in zip(mat1, mat2)]
