def arrayManipulation(n,queries):
    arr=[0]*(n+1)
    # The idea is to use Prefix Sum
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
    
    maximum=temp=0
    for val in arr:
        temp+=1
        maximum=max(temp,maximum)

    return maximum