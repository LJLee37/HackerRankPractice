#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    #retval: left subarray sum == right subarray sum
    lsum = 0
    rsum = sum(arr)
    lenarr = len(arr)
    for i in range(lenarr):
        rsum -= arr[i]
        print(lsum, rsum)
        if lsum == rsum:
            return "YES"
        if lsum > rsum:
            return "NO"
        lsum += arr[i]
    return "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)

    #fptr.close()

