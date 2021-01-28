#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    containerscount = 0
    cur = 0
    lenw = len(w)
    while cur < lenw:
        curcon = w[cur]
        cur += 1
        while cur < lenw and curcon + 4 >= w[cur]:
            cur += 1
        containerscount += 1
    return containerscount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()

