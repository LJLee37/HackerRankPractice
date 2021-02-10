#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    i = 1
    retval = 0
    lenc = len(c)
    ran = range(k)
    while i * k <= lenc:
        for j in ran:
            retval += c[j + (i - 1) * k] * i
        i += 1
    for j in c[(i-1)*k:]:
        retval += j * i
    return retval

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(minimumCost)
    #fptr.write(str(minimumCost) + '\n')

    #fptr.close()

