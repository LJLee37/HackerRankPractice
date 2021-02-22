#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    highest = int(arr[0][0])
    for i in arr:
        if highest < int(i[0]):
            highest = int(i[0])
    li = []
    for i in range(highest + 1):
        li.append([])
    lenarr = len(arr)
    for i in range(lenarr):
        if i < (lenarr // 2):
            li[int(arr[i][0])].append('-')
        else:
            li[int(arr[i][0])].append(arr[i][1])
    for i in li:
        for j in i:
            print(j,end=' ')


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

