#!/bin/python3


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    max_hourglass_sum = float('-inf')
    for i in range(4):
        for j in range(4):
            sum1 = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

            max_hourglass_sum = max(sum1, max_hourglass_sum)
    
    print(max_hourglass_sum)
