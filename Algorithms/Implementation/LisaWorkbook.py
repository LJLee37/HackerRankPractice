#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    retval = 0
    page = 1
    for i in arr:
        for j in range(i):
            if j + 1 == page:
                retval += 1
            if (j + 1) % k == 0 and j + 1 != i:
                page += 1
        page += 1
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

