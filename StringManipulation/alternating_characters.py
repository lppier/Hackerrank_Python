#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    isA = True
    isA = True if s[0]=='A' else False

    count = 0
    for i in range(1,len(s), 1):
        if isA and s[i]=='A':
            count += 1
        elif not isA and s[i]=='B':
            count += 1

        isA = True if s[i]=='A' else False
    
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
