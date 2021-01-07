#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    for i in set(a):
        a.remove(i)
        try:
            a.remove(i)
        except:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

