#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    ler = [[],[arr.pop(0)],[]]
    for i in arr:
        if i < ler[1][0]:
            ler[0].append(i)
        elif i is ler[1][0]:
            ler[1].append(i)
        else:
            ler[2].append(i)
    retval = ler[0] + ler[1] + ler[2]
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

