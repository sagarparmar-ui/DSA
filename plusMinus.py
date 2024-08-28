#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)  # Get the total number of elements in the array
    pos_count = sum(1 for x in arr if x > 0)  # Count positive numbers
    neg_count = sum(1 for x in arr if x < 0)  # Count negative numbers
    zero_count = sum(1 for x in arr if x == 0)  # Count zeros

    # Calculate proportions
    pos_ratio = pos_count / n
    neg_ratio = neg_count / n
    zero_ratio = zero_count / n

    # Print the results with six decimal places
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
