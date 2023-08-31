#!/usr/bin/python3
"""This code is o determmine the perimeter of an island"""


def island_perimeter(grid):
    """island perimeter funvtoin"""
    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:  # If it's land
                perimeter += 4  # Each land cell contributes 4 to perimeter

                # Check adjacent cells
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 if there's land above
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 if there's land to the left

    return perimeter
