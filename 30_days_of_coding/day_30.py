#!/bin/python3

import os

def bitwiseAnd(n, k):
    max_bit = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            bitwise = i & j
            if max_bit < bitwise < k:
                max_bit = bitwise
                if max_bit == k - 1:
                    return max_bit
    return max_bit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        fptr.write(str(res) + '\n')

    fptr.close()
