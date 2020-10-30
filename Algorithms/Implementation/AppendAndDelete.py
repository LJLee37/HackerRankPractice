#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    last = len(s) > len(t) and len(t) or len(s)
    for i in range(last):
        if s[i] != t[i]:
            last = i
            break
    if k >= len(s) + len(t):
        return 'Yes'
    k -= (len(s) - last + len(t) - last)
    if k < 0:
        return 'No'
    if k % 2 == 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
