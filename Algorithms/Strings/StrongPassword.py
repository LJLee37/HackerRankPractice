#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    Numbers = "0123456789"
    Lower_case = "abcdefghijklmnopqrstuvwxyz"
    Upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Special_characters = "!@#$%^&*()-+"
    # Return the minimum number of characters to make the password strong
    lenth = 0
    isContaining = [False, False, False, False] #digit, lower, upper, special
    if n < 6:
        lenth = 6 - n
    for i in password:
        if i in Numbers:
            isContaining[0] = True
        if i in Lower_case:
            isContaining[1] = True
        if i in Upper_case:
            isContaining[2] = True
        if i in Special_characters:
            isContaining[3] = True
    count = isContaining.count(False)
    if lenth < count:
        return count
    else:
        return lenth

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

