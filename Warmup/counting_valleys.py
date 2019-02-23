#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    pos = 0
    valley_cnt = 0
    in_valley = False

    for char in s:
        last_pos = pos
        if char == 'U':
            pos += 1
        elif char == 'D':
            pos -= 1

        if pos == 0:
            in_valley = False

        if last_pos == 0 and pos == -1 and not in_valley:  # new valley
            valley_cnt += 1
            in_valley = True

    return valley_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
