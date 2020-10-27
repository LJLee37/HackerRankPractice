#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    retval = []
    temp = []
    for i in range(len(p)):
        for j in range(len(p)):
            if i + 1 == p[j]:
                temp.append(j+1)
                break
    for i in range(len(p)):
        for j in range(len(p)):
            if temp[i] == p[j]:
                retval.append(j+1)
                break
    return retval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

