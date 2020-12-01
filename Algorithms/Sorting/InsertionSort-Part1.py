#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    isStored = False
    temp = 0
    for i in range(n - 1):
        if isStored:
            if arr[-2-i] > temp:
                arr[-1-i] = arr[-2-i]
            else:
                arr[-1-i] = temp
                isStored = False
                for j in arr:
                    print(j, end=' ')
                print()
                break
            for j in arr:
                print(j, end=' ')
            print()
        else:
            if arr[-1-i] < arr[-2-i]:
                temp = arr[-1-i]
                arr[-1-i] = arr[-2-i]
                isStored = True
            for j in arr:
                print(j, end=' ')
            print()
    if isStored:
        arr[0] = temp
        for j in arr:
            print(j, end=' ')
        print()



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

