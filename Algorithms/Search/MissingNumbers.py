#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    dic = {}
    for i in arr:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    retval = []
    dickeys = dic.keys()
    for i in dickeys:
        if i not in brr:
            retval.append(i)
        elif brr.count(i) != dic[i]:
            retval.append(i)
    for i in set(brr):
        if i not in dickeys:
            retval.append(i)
    retval.sort()
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

