#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    sorted = False
    for i in range(n - 1):
        sorted = True
        temp = 0
        if arr[i] > arr[i + 1]:
            sorted = False
            temp = arr.pop(i + 1)
        if not sorted:
            for j in range(n - 1):
                if temp < arr[j]:
                    arr.insert(j, temp)
                    break
        for j in range(n):
            print(arr[j], end=' ')
        print("")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

