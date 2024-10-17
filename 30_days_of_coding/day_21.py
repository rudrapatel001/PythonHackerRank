#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
total_swap = 0

def swap(i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

for i in range(n):
    swap_no = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            swap(j, j+1)
            swap_no += 1
    total_swap += swap_no
    
    if swap_no == 0:
        break

print(f"Array is sorted in {total_swap} swaps.")
print("First Element: " + str(a[0]))
print(f"Last Element: " + str(a[n-1]))

            
            
            
            
            