def max_pieces(n,a,b,c):
    if n==0:
        return 0
    if n<0:
        return -1
    result= max(max_pieces(n-a,a,b,c),max_pieces(n-b,a,b,c),max_pieces(n-c,a,b,c))
    if result==-1:
        return -1
    return result+1
n=23
print(max_pieces(23,11,9,1))