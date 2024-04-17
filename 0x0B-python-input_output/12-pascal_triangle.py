#!/usr/bin/python3
""" pascal_triangle module
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        if i > 0:
            row.append(1)
        triangle.append(row)
    return triangle
