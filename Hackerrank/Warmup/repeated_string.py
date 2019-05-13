#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    one_s_count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            one_s_count += 1
    repeats = int(n / len(s))
    remainder = int(n - (len(s)*repeats))

    remain_count = 0
    for j in range(remainder):
        if s[j] == 'a':
            remain_count += 1

    count = repeats * one_s_count + remain_count

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
