#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    maxSum = -1
    retval = [-1]
    lensticks = len(sticks)
    for i in range(lensticks - 2):
        if sticks[i] >= sticks[i + 1] + sticks[i + 2]:
            continue
        for j in range(i + 1, lensticks - 1):
            if sticks[i] >= sticks[j] + sticks[j + 1]:
                break
            for k in range(j + 1, lensticks):
                if sticks[i] >= sticks[j] + sticks[k]:
                    break
                if maxSum < sticks[i] + sticks[j] + sticks[k]:
                    maxSum = sticks[i] + sticks[j] + sticks[k]
                    retval = [sticks[k], sticks[j], sticks[i]]
    return retval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

