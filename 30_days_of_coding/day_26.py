import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(5, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

nums = int(input())

for _ in range(nums):
    n = int(input())
    
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
