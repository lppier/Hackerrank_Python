# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:48:16 2019

@author: pier_lim
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict= {}
    for word in magazine:
        if word not in mag_dict:
            mag_dict[word] = 1
        else:
            mag_dict[word] += 1
    
    for word in note:
        if word not in mag_dict:
            print("No")
            return
        else:
            mag_dict[word] -= 1
            if mag_dict[word] == 0:
                del mag_dict[word]
    
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
