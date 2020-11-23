#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    lenc = len(c)
    if lenc == 1:
        if c[0] > n - c[0] - 1:
            return c[0]
        else:
            return n - c[0] - 1
    c.sort()
    temp = [c[0] * 2]
    for i in range(lenc - 1):
        temp.append(c[i + 1] - c[i])
    temp.append((n - c[-1] - 1) * 2)
    return max(temp) // 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

