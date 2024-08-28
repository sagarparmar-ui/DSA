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
    # Calculate the total sum of all five elements
    total_sum = sum(arr)
    
    # Find the minimum and maximum elements in the array
    min_element = min(arr)
    max_element = max(arr)
    
    # Calculate the minimum sum by excluding the maximum element
    min_sum = total_sum - max_element
    # Calculate the maximum sum by excluding the minimum element
    max_sum = total_sum - min_element
    
    # Print the results as two space-separated integers
    print(min_sum, max_sum)

if __name__ == '__main__':
    # Read the input as a list of integers
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)