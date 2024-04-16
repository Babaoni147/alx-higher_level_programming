#!/usr/bin/python3
"""Defining Function"""


def pascal_triangle(n):
    """Represent Pascal triangule of size n.
    Return a list of lists of integers representing the triangule.
    """
    if n <= 0:
        return []

    triangules = [[1]]
    while len(triangules) != n:
        tri = triangules[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangules.append(tmp)
    return triangules
