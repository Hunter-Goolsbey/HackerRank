#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    SumArr = []
  
    minSum = sum(arr) - min(arr)
    maxSum = sum(arr) - max(arr)

    SumArr.append(minSum)
    SumArr.append(maxSum)

    print(SumArr[1], SumArr[0])
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
