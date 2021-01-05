#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    if n is 0: return 1
    log2 = int(math.log2(n)) + 1
    zeros = bin(n ^ int('1'*log2, 2))
    return int(math.pow(2,zeros.count('1')))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()

