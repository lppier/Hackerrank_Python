#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    # Case 1
    for i in range(len(q)):
        ori_idx = q[i] - 1
        if ori_idx - i > 2:
            print("Too chaotic")
            return

    # Case 2
    swap = 0
    for i in range(len(q)):
        for j in range(len(q)-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swap += 1
                swaped = True
        
        # Optimization: If no swapping at all occured for the entire j range, the array is in order
        if swaped:
            swaped = False
        else:
            break
    print(swap)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        if (len(q) == n):
            minimumBribes(q)
        else:
            print("Error size")
