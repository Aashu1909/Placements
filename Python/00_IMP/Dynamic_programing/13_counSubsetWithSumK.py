# Count Subset that are equal to sum K
# This solution works for only when 1<=val<=10**9 
# RECURSIVE+MEMOIZED 
def solve(index,sum,arr,dp):
    if sum==0:
        return 1
    if index==0:
        return 1 if arr[index]==sum else 0
    if (index,sum) in dp:
        return dp[(index,sum)]
    notTake=solve(index-1,sum,arr,dp)
    take=0
    if arr[index]<=sum:
        take=solve(index-1,sum-arr[index],arr,dp)
    dp[(index,sum)]=notTake+take
    return dp[(index,sum)]
    
def countSubsetwithSumK(arr,sum):
    n=len(arr)    
    dp={}
    solve(n-1,sum,arr,dp)


# TABULATION
def countsubsetSum(arr,target):
    n=len(arr)
    dp=[[0 for i in range(target+1)] for _ in range(n)]
    # IF SUM=0 
    # I->index,j-> SUM
    for i in range(n): dp[i][0]=1
    if arr[0]<=target:
        dp[0][arr[0]]=1

    for index in range(1,n):
        for sum in range(target+1):
            notTake=dp[index-1][sum]
            take=0
            if arr[index]<=sum:
                take=dp[index-1][sum-arr[index]]
            dp[index][sum]=notTake+take
    return dp[n-1][target]

