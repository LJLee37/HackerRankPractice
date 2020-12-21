#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    tempResult = re.fullmatch("(.*)h(.*)a(.*)c(.*)k(.*)e(.*)r(.*)r(.*)a(.*)n(.*)k(.*)", s)
    if tempResult is None:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

