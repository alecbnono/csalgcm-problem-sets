#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        firstString = s[0:len(s)//2]
        secondString = s[len(s)//2:]

        freq = {}

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 0

        for i in range(len(firstString)):
            if firstString[i] in freq:
                freq[firstString[i]] += 1

        for i in range(len(secondString)):
            if secondString[i] in freq:
                freq[secondString[i]] -= 1

        total = 0
        for v in freq.values():
            if v > 0:
                total += v
        return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
