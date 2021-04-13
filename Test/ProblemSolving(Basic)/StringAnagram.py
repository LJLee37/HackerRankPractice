#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    temp = set(dictionary)
    counts = {i : dictionary.count(i) for i in temp}
    retval = []
    for i in query:
        if i in temp:
            retval.append(counts[i])
        else:
            retval.append(0)
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(str(sorted(dictionary_item)))

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(str(sorted(query_item)))

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

