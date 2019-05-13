#!/bin/python3

import math
import os
import random
import re
import sys

def createDict(n ,ar):
    adict= {}
    for i in range(n):
        if ar[i] not in adict:
            adict[ar[i]] = 1
        else:
            adict[ar[i]] += 1
    return adict

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    adict = createDict(n, ar)
    print(adict)
    count = 0
    for key in adict:
        count += adict[key] // 2
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
