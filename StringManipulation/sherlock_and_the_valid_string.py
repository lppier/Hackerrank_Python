#!/bin/python3

import math
import os
import random
import re
import sys

def getFreqCountDict(s):
    adict = {}
    for char in s:
        if char in adict:
            adict[char] += 1
        else:
            adict[char] = 1
    print(adict)
    return adict

# Complete the isValid function below.
def isValid(s):
    sdict = getFreqCountDict(s)
    sdict_list = list(sdict.values())
    freq_cnt_dict = getFreqCountDict(sdict_list)
    if len(freq_cnt_dict) > 2:
        return "NO"
    elif len(freq_cnt_dict) == 1:
        return "YES"
    else:
        akey = list(freq_cnt_dict)[0]
        bkey = list(freq_cnt_dict)[1]
        aval = list(freq_cnt_dict.values())[0]
        bval = list(freq_cnt_dict.values())[1]

        if aval > bval: # aabbccc | a:2 b:2 c:3 | 2:2 3:1
            if bkey - akey == 1 or (bkey == 1 and bval == 1):
                return "YES"
            else:
                return "NO"
        elif bval > aval:
            if akey - bkey == 1 or (akey == 1 and aval == 1):
                return "YES"
            else:
                return "NO"
        else: # aval == bval
            return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
