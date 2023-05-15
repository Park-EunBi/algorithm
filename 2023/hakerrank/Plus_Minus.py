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
    # Write your code here
    count = [0, 0, 0]
    length = len(arr)

    for i in arr:
        i = int(i)
        if i > 0:
            count[0] += 1
        elif i < 0:
            count[1] += 1
        else:
            count[2] += 1

    for i in range(3):
        print(count[i] / length)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

'''
<testCode>
6
-4 3 -9 0 4 1
<answer>
0.5
0.3333333333333333
0.16666666666666666
'''