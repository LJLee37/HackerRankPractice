#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    changed = True
    while changed:
        dellist = []
        changed = False
        for i in range(len(s) - 1):
            if i in dellist:
                continue
            if s[i] == s[i + 1]:
                dellist.append(i)
                dellist.append(i + 1)
                changed = True
        l = list(s)
        for i in range(len(dellist)):
            l.pop(dellist[i])
            for j in range(i, len(dellist)):
                dellist[j] -= 1
        s = ''.join(l)
    if s == '':
        s = "Empty String"
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    #fptr.write(result + '\n')

    #fptr.close()
    print(result)
