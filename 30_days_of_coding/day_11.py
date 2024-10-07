
if __name__ == '__main__':
    n = int(input().strip())

def max1s(n):
    max_len = 0
    current_len = 0

    while n > 0:
        bit = n % 2
        
        if bit == 1:
            current_len += 1
            max_len = max(max_len, current_len) 
        else:
            current_len = 0

        n = n // 2

    print(max_len)
    
max1s(n)




