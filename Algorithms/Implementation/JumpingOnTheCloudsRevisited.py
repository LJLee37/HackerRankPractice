#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = 0
    e = 100
    lencloud = len(c)
    i += k
    i %= lencloud
    if c[i]:
        e -= 2
    e -= 1
    while i != 0:
        i += k
        i %= lencloud
        if c[i]:
            e -= 2
        e -= 1
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

