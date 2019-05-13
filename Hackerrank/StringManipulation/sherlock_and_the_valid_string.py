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
    if len(freq_cnt_dict) > 2:  # more than 2 frequencies of char, no way ie. aabbbcccc
        return "NO"
    elif len(freq_cnt_dict) == 1:  # ie. a
        return "YES"
    else:  # there's just 2 entries in this dict, get them
        akey = list(freq_cnt_dict)[0]
        bkey = list(freq_cnt_dict)[1]
        aval = list(freq_cnt_dict.values())[0]
        bval = list(freq_cnt_dict.values())[1]

        # Eg. aabbccc | sdict a:2 b:2 c:3 | freq_cnt_dict akey 2:aval 2   bkey 3:bval 1

        if aval > bval:  # then b is the one from which to remove a char
            # 2 cases, (1) remove 1 char from b such that b is on par with a
            #          (2) remove 1 char (that has 1 occurance)
            if bkey - akey == 1 or (bkey == 1 and bval == 1):
                return "YES"
            else:
                return "NO"
        elif bval > aval:  # this is just exact mirror
            if akey - bkey == 1 or (akey == 1 and aval == 1):
                return "YES"
            else:
                return "NO"
        else:  # aval == bval   ie. aabbcccddd a:2 b:2 c:3 d:3
            return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
