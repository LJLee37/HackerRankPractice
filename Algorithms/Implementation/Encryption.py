#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    lens = len(s)
    sq = math.sqrt(lens)
    li = [9, 9]
    for i in range(math.floor(sq), math.ceil(sq) + 1):
        for j in range(i, math.ceil(sq) + 1):
            if i * j >= lens:
                if i * j < li[0] * li[1]:
                    li[0] = i
                    li[1] = j
    rows, columns = li
    retli = []
    for i in range(rows):
        retli.append(s[i * columns:(i + 1) * columns])
    retli = list(map(list,retli))
    while columns != len(retli[-1]):
        retli[-1].append('')
    retval = []
    for j in range(columns):
        for i in range(rows):
            retval.append(retli[i][j])
        retval.append(' ')
    return ''.join(retval)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

