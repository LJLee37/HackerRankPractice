#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    retval = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            moving = arr[i + 1]
            while arr[i] > moving and i >= 0:
                arr[i + 1] = arr[i]
                retval += 1
                i -= 1
            arr[i + 1] = moving
    return retval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

