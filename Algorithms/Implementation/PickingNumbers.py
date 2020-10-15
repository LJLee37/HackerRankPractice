#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    retval = 0
    prev = 0
    cur = a[0]
    for i in range(len(a)):
        cur = a[i]
        if prev == cur:
            continue
        curval = 1
        for j in range(len(a)):
            if i >= j:
                continue
            if a[i] == a[j] or a[j] - a[i] == 1:
                curval += 1
            else:
                break
        if retval < curval:
            retval = curval
        prev = cur
    return retval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

