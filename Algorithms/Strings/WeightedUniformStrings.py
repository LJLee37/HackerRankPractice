#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    dic = {}
    minus = ord('a') - 1
    for i in list(set(s)):
        dic[ord(i) - minus] = 0
    cur = s[0]
    curcount = 0
    print(dic)
    for i in s:
        if cur == i:
            curcount += 1
        else:
            cur = i
            curcount = 1
        if dic[ord(i) - minus] < curcount:
            dic[ord(i) - minus] = curcount
    retval = []
    dickeys = dic.keys()
    print(dic)
    for i in queries:
        temp = []
        for j in dickeys:
            if i % j == 0:
                temp.append(j)
        yes = False
        for j in temp:
            if i // j <= dic[j]:
                retval.append('Yes')
                yes = True
                break
        if not yes:
            retval.append('No')
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

