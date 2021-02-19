#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    li = []
    isInOrder = True
    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            isInOrder = False
    if isInOrder:
        return sum(arr)
    for i in range(n):
        if i == 0:
            li.append(1)
            continue
        if arr[i] > arr[i - 1]:
            li.append(li[i - 1] + 1)
        elif arr[i] < arr[i - 1]:
            li.append(1)
        else:
            li.append(1)
    isInOrder = False
    while not isInOrder:
        isInOrder = True
        for i in range(1, n):
            if i != 0:
                if arr[i] > arr[i - 1] and li[i] <= li[i - 1]:
                    isInOrder = False
                    li[i] = li[i - 1] + 1
                elif arr[i] < arr[i - 1] and li[i] >= li[i - 1]:
                    isInOrder = False
                    li[i - 1] = li[i] + 1
    return sum(li)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

