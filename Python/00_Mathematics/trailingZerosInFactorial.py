# Naive solution Brute force
def fac(n):
    res=1
    for i in range(2,n+1):
        res=res*i
    return res

def trailing_Zeros(n):
    factorial=fac(n)
    count=0
    while factorial%10==0:
        count+=1
        factorial=factorial//10
    return count


# More Efficient Solution
def trailing_Zeros(n):
    count=0
    i=5
    while n/i>=1:
        count+=(n//i)
        i=i*5
    return count


test_case=100
print(trailing_Zeros(test_case))
