#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#

def calcMissing(readings):
    # Write your code here
    lor= len(readings)
    for line in range(lor):
        if "Missing" in line:
            
if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
