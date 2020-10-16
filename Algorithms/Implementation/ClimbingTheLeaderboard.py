#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def bs(arr, n):
    bsLeft = 0
    bsRight = len(arr) - 1
    bsCurrent = (bsLeft + bsRight) // 2
    while not (n >= arr[bsCurrent] and n < arr[bsCurrent - 1]):
        if bsLeft == bsRight:
            return bsLeft
        if bsLeft > bsRight:
            return -1
        if bsRight - bsLeft == 1:
            if n >= arr[bsRight] and n < arr[bsLeft]:
                return bsRight
            elif n >= arr[bsLeft] and n < arr[bsLeft - 1]:
                return bsLeft
            else:
                return -1
        if n == arr[bsCurrent]:
            return bsCurrent
        elif n >= arr[bsCurrent]:
            bsRight = bsCurrent
        else:
            bsLeft = bsCurrent
        bsCurrent = (bsLeft + bsRight) // 2
    return bsCurrent

def climbingLeaderboard(ranked, player):
    # Write your code here
    retval = []
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    for i in player:
        #print(ranked)
        #print(retval)
        ranklen = len(ranked)
        if i < ranked[ranklen - 1]:
            ranked.append(i)
            retval.append(ranklen + 1)
            continue
        if i == ranked[ranklen - 1]:
            retval.append(ranklen)
            continue
        if i > ranked[0]:
            ranked.insert(0, i)
            retval.append(1)
            continue
        if i == ranked[0]:
            retval.append(1)
            continue
        bsCurrent = bs(ranked, i)
        if i != ranked[bsCurrent]:
            ranked.insert(bsCurrent, i)
        retval.append(bsCurrent + 1)
    return retval

"""
        for j in range(len(ranked)):
            if i >= ranked[j]:
                retval.append(j + 1)
                if i != ranked[j]:
                    ranked.insert(j, i)
                break
                """

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print('\n'.join(map(str, result)))
    print('\n')

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

