#!/bin/python3
#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows = len(arr)
    if rows == 0: return 0
    cols = len(arr[0])
    if cols == 0: return 0

    biggest_hg = -9 * 5 

    for row in range(rows-2):
        for col in range(cols-2):
            hg_sum = 0
            hg_sum = hg_sum + arr[row][col] + arr[row][col+1] + arr[row][col+2]
            hg_sum = hg_sum + arr[row+1][col+1]
            hg_sum = hg_sum + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if hg_sum > biggest_hg:
                biggest_hg = hg_sum


    return biggest_hg

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
