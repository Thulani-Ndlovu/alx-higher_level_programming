#!/usr/bin/python3
'''Function definition'''


def pascal_triangle(n):
    '''Pascal triangle implementation'''
    if n <= 0:
        return []

    pascalTriangle = [[1]]
    while len(pascalTriangle) != n:
        triangle = pascalTriangle[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        pascalTriangle.append(tmp)
    return pascalTriangle
