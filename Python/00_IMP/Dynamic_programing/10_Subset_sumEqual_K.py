# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
# Recurrence call + Memoization

def subsetSumToK(n,arr,k):

    return solve(n-1,k,arr)

def solve(index,target,arr)->bool:
    if target==0:
        return True
    if index==0:
        return (target==arr[index])

    notTake=solve(index-1,target,arr)
    take=False
    if arr[index]<=target:
        take=solve(index-1,target-arr[index],arr)
    return (take or notTake)

def subsetSum(arr,n,k):
    dp=[[False for i in range(k+1)]for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    dp[0][arr[0]]=True
    for index in range(1,n):
        for target in range(1,k+1):        
            notTake=dp[index-1][target]
            take=False
            if arr[index]<=target:
                take=dp[index-1][target-arr[index]]
            dp[index][target]=(notTake or take)

    return dp[n-1][k]
                
arr=[3, 34, 4, 12, 5, 2]
sm=9
print(subsetSumToK(len(arr),arr,sm))
print(subsetSum(arr,len(arr),sm))