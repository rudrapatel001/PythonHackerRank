

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

temp = []

for i in range(len(arr)):
    
    temp.insert(0, arr[i])
    
print(' '.join(map(str, temp)))
