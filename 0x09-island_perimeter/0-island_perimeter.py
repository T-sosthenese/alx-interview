#!/usr/bin/python3
"""
A module that computes the perimeter of an island
"""


def island_perimeter(grid):
    """Returns the perimeter of the island
    """
    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4
                if grid[i - 1][j] == 1:
                    perimeter -= 2
                if grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
