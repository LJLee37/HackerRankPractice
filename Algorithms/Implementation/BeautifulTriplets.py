#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    retval = 0
    la = len(arr)
    """for i in range(la):
        for j in range(i + 1, la):
            for k in range(j + 1, la):
                if arr[j] - arr[i] == d and arr[k] - arr[j] == d:
                    retval += 1
    TLE                """
    li = {}
    for i in range(la):
        if arr[i] in li.keys():
            li[arr[i]] += arr.count(arr[i] + d)
        else:
            li[arr[i]] = arr.count(arr[i] + d)
    k = li.keys()
    for i in k:
        if i + d in k:
            retval += li[i] * li[i + d]
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

