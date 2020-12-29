#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    rowG = len(G)
    rowP = len(P)
    colG = len(G[0])
    colP = len(P[0])
    found = False
    for i in range(rowG - rowP + 1):
        for j in range(colG - colP + 1):
            #print(G[i][j:j + colP], P[0])
            if G[i][j:j + colP] == P[0]:
                found = True
                for k in range(rowP):
                    if G[i + k][j:j + colP] != P[k]:
                        found = False
                        break
                if found:
                    return 'YES'
    if found:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)
    #    fptr.write(result + '\n')
    #fptr.close()

