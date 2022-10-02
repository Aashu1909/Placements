from bisect import bisect_left as lower_bound
def minPartition(N):
    # code here
    coins=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    m=len(coins)
    ans=[]
    while N>0:
        idx=lower_bound(coins,N)
        print(ans)
        print
        if idx>m :
            N-=coins[idx-1]
            ans.append(coins[idx-1])
        else:
            N-=coins[idx]
            ans.append(coins[idx])

    return ans
n=8098
print(minPartition(n))