#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    retval = []
    retval.append(len(arr))
    while(True):
        isAllSame = True
        temp = arr[0]
        for i in arr:
            if i != temp:
                isAllSame = False
                break
        if isAllSame:
            break
        smallest = arr[0]
        for i in arr:
            if i < smallest:
                smallest = i
        for i in range(len(arr)):
            arr[i] -= smallest
        for i in range(len(arr)):
            try:
                arr.remove(0)
            except:
                break
        retval.append(len(arr))
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

