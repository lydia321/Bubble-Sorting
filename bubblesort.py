#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product
#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count=0;
    # Write your code here
    for i,j in product(range(len(a)),range(len(a)-1)):
             if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                count+=1
    print("Array is sorted in %s swaps." %count)
    print("First Element:", a[0])
    print("Last Element:", a[-1])       

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
