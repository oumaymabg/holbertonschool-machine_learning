#!/usr/bin/env python3
"""The transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """The matrix transpose"""
    nrows = len(matrix)
    ncols = len(matrix[0])
    transpose = [[0 for _ in range(nrows)] for _ in range(ncols)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transpose[j][i] = matrix[i][j]
    return transpose