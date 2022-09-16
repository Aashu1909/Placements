def jos(n,k):
    if n==1:
        return 0
    else:
        return (jos(n-1,k)+k) % n

def myjos(n,k):
    return jos(n,k)+1
print(myjos(6,2))