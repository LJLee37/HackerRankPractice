#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    s = list(s)
    k %= 26
    for i in range(len(s)):
        if s[i] >= 'A' and s[i] < chr(ord('Z') - k + 1):
            s[i] = chr(ord(s[i]) + k)
        elif s[i] >= 'a' and s[i] < chr(ord('z') - k + 1):
            s[i] = chr(ord(s[i]) + k)
        elif s[i] >= chr(ord('Z') - k + 1) and s[i] <= 'Z':
            s[i] = chr(ord(s[i]) - (ord('Z') - k + 1) + ord('A'))
        elif s[i] >= chr(ord('z') - k + 1) and s[i] <= 'z':
            s[i] = chr(ord(s[i]) - (ord('z') - k + 1) + ord('a'))
    return ''.join(s)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    #fptr.write(result + '\n')

    #fptr.close()

    print(result)
