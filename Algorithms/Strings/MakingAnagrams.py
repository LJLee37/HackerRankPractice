#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def makingAnagrams(s1, s2):
    splited = [s1, s2]
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
            diff.append(abs(alphaCount[0][i] - alphaCount[1][i]))
    return sum(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
