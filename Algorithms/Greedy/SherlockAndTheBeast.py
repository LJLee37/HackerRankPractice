#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    fives = 0
    while (n % 3 != 0) and (n >= 0):
        fives += 1
        n -= 5
    if n < 0:
        print(-1)
    else:
        print('5'*(n//3)*3+'3'*fives*5)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

