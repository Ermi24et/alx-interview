#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island"""
    n = len(grid)
    m = len(grid[0])

    def check_side(r, c):
        if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
            return 1
        if grid[r][c] == 1:
            grid[r][c] = 2
            return (check_side(r-1, c) +
                    check_side(r+1, c) +
                    check_side(r, c-1) +
                    check_side(r, c+1))
        return 0

    perimeter = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                perimeter += check_side(r, c)
    return perimeter
