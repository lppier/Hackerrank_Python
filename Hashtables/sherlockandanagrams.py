# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:47:07 2019

@author: pier_lim
"""

#!/bin/python3

import math
import os
import random
import re
import sys




from collections import Counter

def sherlockAndAnagrams(s):
    counts = 0
    
    ahash = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1, 1):
            sub = s[i:j]
            sub = ''.join(sorted(sub))
            if sub not in ahash:
                ahash[sub] = 1
            else:
                ahash[sub] += 1
    
    sum = 0
    for i in ahash:
        n = ahash[i]
        sum += (n*(n-1))/2
    print(sum)
    
    return int(sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
