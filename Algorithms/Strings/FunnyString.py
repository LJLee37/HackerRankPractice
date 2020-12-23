#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    li = list(s)
    li = list(map(ord,li))
    sub1 = []
    for i in range(len(li) - 1):
        sub1.append(abs(li[i] - li[i + 1]))
    sub2 = list(reversed(sub1))
    if sub1 == sub2:
        return 'Funny'
    else:
        return 'Not Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

