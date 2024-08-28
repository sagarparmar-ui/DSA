#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):

    arr.sort()      # Sort the array
    
    n = len(arr)    # Calculate the middle index
    mid = n // 2
    
    if n % 2 == 1:  # Return the median based on the length of the array
        return arr[mid]    # If odd, return the middle element
    else:
        return (arr[mid - 1] + arr[mid]) // 2     # If even, return the average of the two middle elements

if __name__ == '__main__':
    # Read the input array
    arr = list(map(int, input().rstrip().split()))
    # Find the median
    result = findMedian(arr)
    # Print the result
    print(result)