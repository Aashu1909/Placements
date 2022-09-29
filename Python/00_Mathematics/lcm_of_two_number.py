# Naive Or Brute Force
def lcm(a,b):
    max_of_two=max(a,b)
    while True:
        if max_of_two%a==0 and max_of_two%b==0:
            break
        max_of_two+=1
    return max_of_two

# Efficient solution 
# A*B=gcd(a,b)*lcm
def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def lcm_using_gcd(a,b):
    return a*b//gcd(a,b)




a,b=5,6
print(lcm_using_gcd(a,b))