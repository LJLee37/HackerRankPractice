#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    li = {}
    ds = []
    for i in range(len(a)):
        if a[i] in li.keys():
            ds.append(i - li[a[i]])
        else:
            li[a[i]] = i
    if len(ds) == 0:
        return -1
    ds.sort()
    return ds[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

