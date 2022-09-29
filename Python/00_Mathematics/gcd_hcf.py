def gcd(a,b):
    minimum_of_two=min(a,b)
    while minimum_of_two>0:
        if a%minimum_of_two==0 and b%minimum_of_two==0:
            break
        minimum_of_two-=1
    result=minimum_of_two
    return result

# Efficient is eucladian Algorithm 
def gcd1(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a