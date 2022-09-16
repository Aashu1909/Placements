# Q.Find all prime number smaller than N
# Naive mehod
import math
def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3 or n==5:
        return True
    if n%2==0 or n%3==0 or n%5==0:
        return False
    i=2
    while (int(math.sqrt(n))//i):
        if n%i==0:
            return False
        i=i+1
    return True

def printPrime(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i,end=" ")
    print()

# efficient solution
def SieveOfEratosthene(n):
    if n<=1:
        return 
    prime_lst=[True]*(n+1)
    prime_lst[0],prime_lst[1]=False,False
    print(prime_lst)
    # [False, False, True, True, True, True, True, True, True]
    # [ 0  ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ,  8  ]
    i=2
    while n//(i*i)>=1:
        if isPrime(i):
            print(i)
            j=2*i
            while j<=n:
                prime_lst[j]=False
                j=j+i
        i=i+1
    print(prime_lst)
    # [True, True, True, True, False, True, False, True, False]
    # [ 0  ,  1  ,  2  ,  3  ,  4  ,   5  ,  6  ,   7  ,  8  ]
    for i in range(2,n+1):
        if prime_lst[i]:
            print(i,end=" ")


test=8
print(SieveOfEratosthene(test))