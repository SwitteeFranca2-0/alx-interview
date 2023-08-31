#!/usr/bin/python3
"""This code is o determmine the perimeter of an island"""


def island_perimeter(grid):
    """This function finds the area of the island perimeter"""
    height = len(grid)
    width = len(grid[0])
    length = 0
    breadth = 0
    for row in grid:
        if 1 not in row and length != 0:
            break
        if 1 in row:
            length += 1
            if row.count(1) > breadth:
                breadth = row.count(1)
    return 2*(length + breadth)
