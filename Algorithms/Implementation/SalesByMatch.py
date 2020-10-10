#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    retval = 0
    li = []
    for i in range(n):
        for j in range(i + 1, n):
            if ar[i] is ar[j]:
                if i not in li:
                    li.append(i)
                    li.append(j)
                    retval += 1
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
