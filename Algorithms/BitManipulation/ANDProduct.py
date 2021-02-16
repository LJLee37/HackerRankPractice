#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def andProduct(a, b):
    if b >= a * 2:
        return 0
    if a == b:
        return a
    retval = a & b
    avg = (a + b) // 2
    retval &= avg
    bma = b - a
    n = 1
    two = False
    while 2 ** n < bma:
        retval &= ((2 ** (n - 1)) ^ 0b11111111111111111111111111111111)
        n += 1
        """
    if b >= 2 ** n:
        retval &= 2 ** n
        if retval == 0:
            return 0
        two = True
    ran = range(2 ** n, b) if two else range(a + 1, b)
    for i in ran:
        retval &= i
        if retval == 0:
            return retval
            """
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

