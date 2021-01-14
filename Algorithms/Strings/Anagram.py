#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    lens = len(s)
    if lens % 2 != 0:
        return -1
    splited = [s[:lens//2], s[lens//2:]]
    alphaCount = [{},{}]
    asciia = ord('a')
    for i in range(26):
        alphaCount[0][chr(i + asciia)] = 0
        alphaCount[1][chr(i + asciia)] = 0
    for i in range(2):
        for j in splited[i]:
            alphaCount[i][j] += 1
    diff = []
    for i in alphaCount[0].keys():
        if alphaCount[0][i] != alphaCount[1][i]:
            diff.append(alphaCount[0][i] - alphaCount[1][i])
    if sum(diff) != 0:
        return -1
    retval = 0
    for i in diff:
        if i > 0:
            retval += i
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

