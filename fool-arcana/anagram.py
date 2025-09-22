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
    # if odd length, can't split evenly
    if len(s) % 2 != 0:
        return -1
    
    # split into two halves
    mid = len(s) // 2
    first, second = s[:mid], s[mid:]
    
    # count characters in each half
    freq_first = {}
    for ch in first:
        freq_first[ch] = freq_first.get(ch, 0) + 1
    
    # subtract chars found in second half
    for ch in second:
        if ch in freq_first and freq_first[ch] > 0:
            freq_first[ch] -= 1
    
    # sum leftover (these must be changed)
    return sum(freq_first.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
