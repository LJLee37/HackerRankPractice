#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    nonImportant = 0
    important = []
    for i in contests:
        if i[1] is 1:
            important.append(i[0])
        else:
            nonImportant += i[0]
    important.sort()
    for i in range(len(important) - k):
        nonImportant -= important.pop(0)
    for i in important:
        nonImportant += i
    return nonImportant

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

