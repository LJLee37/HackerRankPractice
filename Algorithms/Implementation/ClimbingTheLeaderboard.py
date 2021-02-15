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

def search(target, li, lenli):
    prefix = 0
    while True:
        if lenli <= 3:
            for i in range(lenli):
                if target >= li[i]:
                    return prefix + i
            return lenli + prefix
        isOdd = 0
        if lenli % 2 == 1:
            isOdd = 1
        #half = lenli // 2
        median = li[lenli // 2]
        if (target >= median and target < li[lenli // 2 - 1]):
            return lenli // 2 + prefix
        if target > median:
            li = li[:lenli // 2]
            lenli = lenli // 2
        else:
            prefix += lenli // 2 + 1
            li = li[lenli // 2 + 1:]
            lenli = lenli // 2 - 1 + isOdd
    """
    #lenli = len(li)
    if lenli <= 3:
        for i in range(lenli):
            if target >= li[i]:
                return i
        return lenli
    isOdd = 0
    if lenli % 2 == 1:
        isOdd = 1
    half = lenli // 2
    median = li[half]
    if (target >= median and target < li[half - 1]):
        return half
    if target > median:
        return search(target, li[:half], half)
    else:
        return half + search(target, li[half + 1:], half - 1 + isOdd) + 1
        """


def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    retval = []
    lenran = len(ranked)
    lenpl = len(player)
    """
    for i in player:
        retval.append(1 + search(i, ranked, lenran))
        if retval[-1] - 1 == lenran or i != ranked[retval[-1] - 1]:
            ranked.insert(retval[-1] - 1, i)
            lenran += 1
    """
    player.reverse()
    curran = 0
    curpl = 0
    while curpl < lenpl and curran < lenran:
        if player[curpl] >= ranked[curran]:
            retval.insert(0, curran + 1)
            curpl += 1
        else:
            curran += 1
    for i in range(curpl, lenpl):
        retval.insert(0, lenran + 1)
    return retval

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

