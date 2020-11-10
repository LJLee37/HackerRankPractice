#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic, n, m):
    retval = [0,0]
    total = []
    for i in range(n):
        for j in range(i + 1, n):
            ts = 0
            for k in range(m):
                if (topic[i][k] == '1' or topic[j][k] == '1'):
                    ts += 1
            total.append(ts)
            if retval[0] < total[-1]:
                retval[0] = total[-1]
    retval[1] = total.count(retval[0])
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic, n, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

