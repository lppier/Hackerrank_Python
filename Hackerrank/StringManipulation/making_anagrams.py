L#!/bin/python3

import math
import os
import random
import re
import sys

def populate_dict(a):
    adict = {}
    for char in a:
        if char in adict:
            adict[char] += 1
        else:
            adict[char] = 1
    
    return adict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    
    adict = populate_dict(a)
    bdict = populate_dict(b)

    count = 0 
    for i in range(97, 123, 1): # a to z
        if (chr(i) not in adict) and (chr(i) in bdict):
            count += bdict[chr(i)]
        elif (chr(i) in adict) and (chr(i) not in bdict):
            count += adict[chr(i)]
        elif (chr(i) in adict) and (chr(i) in bdict):
            count+= abs(adict[chr(i)] - bdict[chr(i)])
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
