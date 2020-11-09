#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    tempdict = {}
    for i in arr:
        if i not in tempdict.keys():
            tempdict[i] = 1
        else:
            tempdict[i] += 1
    max = arr[0]
    for key, val in tempdict.items():
        if tempdict[max] < val:
            max = key
    return len([x for x in arr if x != max])



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

