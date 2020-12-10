#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    mid = len(arr)//2
    if arr[mid] is V:
        return mid
    if arr[mid] < V:
        return mid + introTutorial(V, arr[mid:])
    else:
        return introTutorial(V, arr[:mid])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

