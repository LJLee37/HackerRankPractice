#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    while len(n) != 1 or k > 1:
        li = list(map(int, n))
        retval = 0
        for i in li:
            retval += i
        retval *= k
        n = str(retval)
        k = 1
    return n

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

