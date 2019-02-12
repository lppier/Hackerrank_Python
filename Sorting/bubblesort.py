#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swap = 0
    for i in range(len(a)):
        for j in range(0, len(a)-1, 1):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1]
                swap += 1
    print("Array is sorted in {0} swaps.".format(swap))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[len(a)-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
