# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())  # number of entries
d1 = {}
query = input()
for i in range(n):
    entry = input().split()
    key = entry[0]
    value = entry[1]
    d1[key] = value


    
    
if query in d1:
    print(f"{query}={d1[query]}")
else:
    print("Not found")
