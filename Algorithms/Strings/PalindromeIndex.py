#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    lens = len(s)
    retval = -1
    for i in range(lens // 2):
        if s[i] != s[-1-i]:
            if retval != -1:
                return -1
            else:
                if s[i] == s[-2-i] and s[i + 1] == s[-1-i]:
                    p = 2
                    while i + p < lens // 2:
                        if s[i + p] != s [-i-p]:
                            retval = lens - 1 - i
                            s.pop(-1-i)
                            break
                        p += 1
                    if retval == -1:
                        retval = i
                        s.pop(i)
                elif s[i] == s[-2-i]:
                    retval =  lens-1-i
                    s.pop(-1-i)
                elif s[i + 1] == s[-1-i]:
                    retval = i
                    s.pop(i)
                else:
                    return -1
    return retval

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = list(input())

        result = palindromeIndex(s)
        print(result)
    #    fptr.write(str(result) + '\n')

    #fptr.close()

