#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def timeConversion(s):
    # Extract the period (AM/PM)
    period = s[-2:]
    # Extract the hour, minute, and second from the time string
    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]
    
    # Convert hour based on AM/PM period
    if period == 'AM':
        if hour == 12:
            hour = 0  # Midnight case
    else:
        if hour != 12:
            hour += 12  # Convert PM hour to 24-hour format
    
    # Format hour to be two digits
    hour_24 = f"{hour:02}"
    
    # Return the time in 24-hour format
    return f"{hour_24}:{minute}:{second}"

if __name__ == '__main__':
    s = input().strip()  # Read input time string
    result = timeConversion(s)  # Convert time to 24-hour format
    print(result)  # Print the result