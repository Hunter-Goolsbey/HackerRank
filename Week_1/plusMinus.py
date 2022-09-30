#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    x = []
    y = []
    z = []

    c = len(arr)
    for i in arr:
        
        if (i < 0):
            x.append(i)
            #print(str(len(x)/c) + ' is a negative number')
            
        elif (i > 0):
            y.append(i)
            #print(str(len(x)/c) + ' is a positive number')
            
        else:
            z.append(i)
            #print(str(len(x)/c) + ' is zero')

    print(round(len(y)/c, 6))
    print(round(len(x)/c, 6))
    print(round(len(z)/c, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
