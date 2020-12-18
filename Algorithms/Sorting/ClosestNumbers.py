#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    smallList = []
    smallest = -1
    for i in range(len(arr) - 1):
        if smallest == -1:
            smallest = arr[i + 1] - arr[i]
            smallList.append(arr[i])
            smallList.append(arr[i + 1])
        elif smallest > arr[i + 1] - arr[i]:
            smallest = arr[i + 1] - arr[i]
            smallList.clear()
            smallList.append(arr[i])
            smallList.append(arr[i + 1])
        elif smallest == arr[i + 1] - arr[i]:
            smallList.append(arr[i])
            smallList.append(arr[i + 1])
    return smallList

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

