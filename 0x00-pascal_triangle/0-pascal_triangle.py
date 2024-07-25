#!/usr/bin/python3

"""
Module to implement a pascal triangle
"""


def pascal_triangle(n):
    """
    Function to return a list of lists of integers representing the
    Pascal’s triangle of n

    Args:
        n (int): The number of rows to generate for Pascal's Triangle

    Returns:
        List[List[int]]: List of lists representing Pascal’s Triangle
    """
    if n <= 0:
        return []
    row = [[1]]
    for i in range(1, n):
        new_row = [1]
        for j in range(1, i):
            new_row.append(row[i - 1][j - 1] + row[i - 1][j])
        new_row.append(1)
        row.append(new_row)

    return row
