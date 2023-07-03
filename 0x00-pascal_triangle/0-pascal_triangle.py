#!/usr/bin/python3

def pascal_triangle(n):
    """Create the pascal's triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(0, n):
        nums = []
        for j in range(i, -1, -1):
            num = int(f(i) / (f(i-j)*f(j)))
            nums.append(num)
        triangle.append(nums)
    return (triangle)


def f(num):
    """Find the factrial of the number, num"""
    factorial = 1
    if num == 0:
        return factorial
    for i in range(num, 0, -1):
        factorial *= i
    return factorial
