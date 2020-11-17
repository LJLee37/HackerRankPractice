    #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    # sum = temp2 / 2 * (p + p - (temp2 - 1) * d)
    if p > s :
        return 0
    if 2 * p - d > s:
        return 1
    temp1 = p - m
    temp2 = math.ceil(temp1 / d)
    temp3 = temp2 / 2 * (2 * p - (temp2 - 1) * d)
    if temp3 <= s:
        if temp3 > s - m:
            return int(temp2)
        else:
            return int(temp2 + (s - temp3) // m)
    else:
        bsm4ac = (2 * p) ** 2 + 4 * p * d + d ** 2 - 8 * d * (temp3 - s) >= 0
        if bsm4ac >= 0:
            if bsm4ac == 0:
                return int(2 * p - d)
            temp4 = math.sqrt(bsm4ac)
            if (2 * p + d) >= temp4:
                return int(2 * p + d - temp4)
            else:
                return int(2 * p + d + temp4)

    # n(a1 + a1 - (n - 1)d) / 2 = sum
    # 2an - n^2d + nd = 2sum
    # dn^2 - (2a + d)n + 2sum = 0
    # (2a + d +- sqrt(4a^2 + 4ad + d^2 - 8d(temp3 - s)) / 2d

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(answer)
    #fptr.write(str(answer) + '\n')

    #fptr.close()

