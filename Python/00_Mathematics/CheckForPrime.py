# Naive Or BRute Force method O(N)
def isPrime(n):
    print("1")
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
# Efficient Solution O(sqrt(N))
import math
def isPrime(n):
    print("2")
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

# # More Efficent solution
# def isPrime(n):
#     print("3")
#     if n==1:
#         return False
#     if n==2 or n==3 or n==5:
#         return True
    
#     if n%2==0 or n%3==0 or n%5==0:
#         return False
#     for i in range(2,int(math.sqrt(n))):
#         if n%i==0:
#             return False
#     return True

test=4
print(isPrime(4))