#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    dic = {}
    for i in s:
        if i in dic.keys():
            continue
        else:
            dic[i] = s.count(i)
    dickeys = list(dic.keys())
    possible = False
    li = []
    for i in range(len(dickeys) - 1):
        for j in range(i + 1, len(dickeys)):
            temp = list(s)
            for k in dickeys:
                if k != dickeys[i] and k != dickeys[j]:
                    while k in temp:
                        temp.remove(k)
            cur = True
            for k in range(len(temp) - 1):
                if temp[k] == temp[k + 1]:
                    cur = False
                    break
            if cur:
                li.append(len(temp))
                possible = True
    if possible:
        li.sort()
        return li[-1]
    return 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

