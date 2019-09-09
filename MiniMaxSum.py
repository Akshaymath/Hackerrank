import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s1=0
    s2=0

    for i in range (len(arr)):
        for j in range (0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    for i in range (0,len(arr)-1):
        s1+=arr[i]
    for i in range (1,len(arr)):
        s2+=arr[i]

    s=[s1,s2]
    return s

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    ar=miniMaxSum(arr)
    for i in ar:
        print(i, end=' ')
