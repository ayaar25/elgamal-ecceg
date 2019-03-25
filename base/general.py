from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b)

def inverse(a,b):
    a = a % b; 
    for x in range(1, b) : 
        if ((a * x) % b == 1) : 
            return x 
    return 1
    

# if __name__ == "__main__":
#     print(gcd(9,7))
#     print(inverse(17,7))