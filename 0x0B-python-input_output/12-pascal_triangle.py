#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle"""
    if n <= 0:
        return []

    trian = [[1]]
    while len(trian) != n:
        tr = trian[-1]
        temp = [1]
        for i in range(len(tr) - 1):
            temp.append(tr[i] + tr[i + 1])
        temp.append(1)
        trian.append(temp)
    return trian
