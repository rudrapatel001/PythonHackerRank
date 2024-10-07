t = int(input())
for _ in range(t):
    s = input()
    even = ""
    odd = ""
    
    
    for i, char in enumerate(s):
        if i % 2 == 0:
            even += char
        else:
            odd += char
            
    
    print(even + " " + odd)
    