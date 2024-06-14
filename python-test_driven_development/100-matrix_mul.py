#!/usr/bin/python3
"""
This module provides a function for matrix multiplication.

The function matrix_mul performs matrix multiplication on two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a[1:]):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b[1:]):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            value = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(value)
        result.append(row)

    return result
