#!/bin/python3

import math
import os
import random
import re
import sys

def helper(a, b, memo):
    if a == b:
        return True
    elif len(a)==0:
        return False
    elif len(b)==0:
        # check if a is all smaller case, so that we can remove
        if a.islower():
            return True 
        return False

    lhs_ans = rhs_ans = False

    # removal of 1st char option
    if a[0].islower(): 
        a_new = a[1:]
        if (a_new, b) not in memo:
            lhs_ans = helper(a_new, b,memo)
            memo[(a_new, b)] = lhs_ans
        else:
            lhs_ans = memo[(a_new, b)]
    
    if lhs_ans == True:
        return True
    # capitalizing 1st char and matching option
    if a[0].upper() == b[0]:
        a_new = a[1:]
        b_new = b[1:]
        if (a_new, b_new) not in memo:
            rhs_ans = helper(a_new, b_new, memo)
            memo[(a_new, b_new)] = rhs_ans
        else:
            rhs_ans = memo[(a_new, b_new)]

    if rhs_ans == True:
        return True
    
    return False
# Complete the abbreviation function below.
def abbreviation(a, b):
    memo = {}
    if helper(a, b, memo) is True:
        return "YES"
    else:
        return "NO"

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    sys.setrecursionlimit(2000)

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
