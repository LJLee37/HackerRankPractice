#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    s = list(set(s))
    lens = len(s)
    while True:
        isFinished = True
        tempdic = {}
        key = []
        for i in range(lens - 1):
            for j in range(i + 1, lens):
                if (s[i] + s[j]) % k == 0:
                    isFinished = False
                    if s[i] not in key:
                        tempdic[s[i]] = 1
                        key.append(s[i])
                    else:
                        tempdic[s[i]] += 1
                    if s[j] not in key:
                        tempdic[s[j]] = 1
                        key.append(s[j])
                    else:
                        tempdic[s[j]] += 1
        if isFinished:
            break
        largest = key[0]
        for i in key:
            if tempdic[i] > tempdic[largest]:
                largest = i
        s.remove(largest)
        lens -= 1
        print(s)
    return lens
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

