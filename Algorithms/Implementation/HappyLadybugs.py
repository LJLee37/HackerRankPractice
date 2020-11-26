#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    bugs = []
    bugsmorethan2 = []
    isSpace = False
    for i in b:
        if i == '_':
            isSpace = True
            continue
        if i not in bugs:
            bugs.append(i)
        elif i not in bugsmorethan2:
            bugsmorethan2.append(i)
    for i in bugs:
        if i not in bugsmorethan2:
            return 'NO'
    if isSpace:
        return 'YES'
    prev = b[0]
    isAdjecent = False
    for i in range(len(b) - 1):
        if b[i + 1] == prev:
            isAdjecent = True
        elif isAdjecent is False:
            return 'NO'
        else:
            isAdjecent = False
            prev = b[i + 1]
    if isAdjecent:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

