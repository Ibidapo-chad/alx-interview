#!/usr/bin/python3
"""
Generate a list of lists of integers representing the Pascal's triangle
"""

def factorial(n):
    """Recursively calculate the factorial of a number"""
    if n <= 1:
        return 1
    for c in range(n, 0, -1):
        return c * factorial(c - 1)

def calculate_pascal_value(n, k):
    """Apply formula to calculate value of pascal's triangle directly"""
    return (factorial(n) / (factorial(k) * factorial(n - k)))

def pascal_triangle(n):
    """Returns list of lists of integers representing Pascal's triangle of n"""
    if n <= 0:
        return []
    res = [[1]]
    for x in range(1, n):
        res_temp = []
        for y in range(0, x + 1):
            res_temp.append(int(calculate_pascal_value(x, y)))
        res.append(res_temp)
    return res

