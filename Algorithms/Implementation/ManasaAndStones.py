#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    li = []
    for i in range(n - 1):
        if i == 0:
            temp = {a, b}
            li.append(temp)
        else:
            temp = set([])
            for j in li[-1]:
                temp.add(j + a)
                temp.add(j + b)
            li.append(temp)
    retval = list(li[-1])
    retval.sort()
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

