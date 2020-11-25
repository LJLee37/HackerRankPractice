#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    grid = list(map(list, grid))
    for i in range(len(grid) - 1):
        if i == 0:
            continue
        for j in range(len(grid[0]) - 1):
            if j == 0:
                continue
            if grid[i - 1][j] == 'X' or grid[i + 1][j] == 'X' or grid[i][j - 1] == 'X' or grid[i][j + 1] == 'X':
                continue
            if int(grid[i][j]) > int(grid[i - 1][j]) and int(grid[i][j]) > int(grid[i + 1][j]) and int(grid[i][j]) > int(grid[i][j - 1]) and int(grid[i][j]) > int(grid[i][j + 1]):
                grid[i][j] = 'X'
    grid = list(map(''.join, grid))
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

