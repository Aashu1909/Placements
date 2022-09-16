# def s(arr,n,k):
#     ans=[]
#     maximum=0
#     for i in range(k):
#         maximum=max(maximum,arr[i])
#     ans.append(maximum)
#     i=0
#     while i<n-k:
#         maximum=max(maximum,arr[i+k])
#         ans.append(maximum)
#         i+=1
#     return ans
# print()


from re import A
from shutil import register_unpack_format


def solve1(a,b,c):
    if((1+a)<(b) or (c+3)>3):
        b=b+9
        if((a+b+c)<(c+6)):
            a=(a+a)+b
        
        c=b+a
    # b=(a+3)+b
    return a+b+c
# print(solve1(1,2,10))
def solve(a,b):
    if((2>b) and (2^b)>(b+a)):
        a=(b+2)+a
        a=2+a+b
        # b=(b+3)+a
        b=1+b+b
        # a=(a+2)+a
        return solve(a,b+a)+a+solve(a,b)
    a=2+b
    return a-b+1
# print(solve(a=0,b=0))

def solve(a,b,c=0):
    for c in range(5,9):
        if((c&b)<(7-c)):
            b=12+a
        a=9+a
        b=c+4+a
    return a+b
print(solve(a=0,b=4,c=4))
# print(13^9)