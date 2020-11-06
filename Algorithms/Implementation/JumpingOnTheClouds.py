#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    retval = 0
    i = 0
    l = len(c)
    while i < l:
        if i == l - 1:
            return retval
        if i == l - 2:
            return retval + 1
        if c[i + 2] == 1:
            i += 1
            retval += 1
        else:
            i += 2
            retval += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

