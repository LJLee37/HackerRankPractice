#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    #hourglassPreset = [[0,0],[0,1],[0,2],[1,1],[2,0],[2,1],[2,2]]
    rows = len(arr)
    columns = len(arr[0])
    retval = -999999999999999
    for i in range(rows - 2):
        for j in range(columns - 2):
            currentSum = 0
            currentSum += sum(arr[i][j:j+3])
            currentSum += arr[i + 1][j + 1]
            currentSum += sum(arr[i + 2][j:j + 3])
            if currentSum > retval:
                retval = currentSum
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

