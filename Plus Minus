#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    le=len(arr)
    posco=0
    negco=0
    zerco=0
    for i in range(le):
        a=arr[i]
        if (a==0):
            zerco+=1
        elif (a>0):
            posco+=1
        elif (a<0):
            negco+=1
    posco=posco/le
    negco=negco/le
    zerco=zerco/le

    print(posco)
    print(negco)
    print(zerco)

    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
