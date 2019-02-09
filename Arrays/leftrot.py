#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    b = a.copy()
    for i in range(len(a)):
        new_pos = None
        if i-d >= 0:
            new_pos = i - d
        else:
            new_pos = i - d + len(a)

        b[new_pos] = a[i]

    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
