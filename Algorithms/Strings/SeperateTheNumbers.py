#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s) is 1:
        print("NO")
        return
    init = 0
    temp = 0
    prev = 0
    yes = True
    curlen = 0
    for i in range(len(s)):
        if i is 0:
            init = int(s[0])
            temp = init
        elif curlen is 0:
            

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

