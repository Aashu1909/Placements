# Naive method
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

def primeFactors(n):
    for i in range(2,n):
        if (isPrime(i)):
            x=i
            # if the number is divisible by power of i
            while n%x==0:
                print(i)
                x=x*i
# Optimized Solution
def primeFactors(n):
    if n<=1:
        return 
    i=2
    while n//(i*i)>=1:
        while (n%i==0):
            print(i)
            n=n//i
        i=i+1
    



test_case=12
primeFactors(test_case)