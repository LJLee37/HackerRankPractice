#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    fromFirst = math.ceil((p - 1) / 2) # (11 - 1) / 2 = 5, ceil(5) = 5
    fromLast = n - p # 12 - 11 = 1
    if n % 2 == 0: # 12 % 2 = 0, run.
        fromLast = math.ceil(fromLast / 2) # 1 / 2 = 0.5, ceil(0.5) = 1
    else:
        fromLast = fromLast // 2
    if fromFirst > fromLast: # 
        return fromLast
    else:
        return fromFirst


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print (result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
