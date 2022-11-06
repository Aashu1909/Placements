def minimumSubsetSumDifference(arr,n):
    totalSum=0
    for i in range(len(arr)):
        totalSum+=arr[i]

    dp=[[False for _ in range(totalSum+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0]=True

    if arr[0]<=totalSum:dp[0][arr[0]]=True
    
    for index in range(1,n):
        for target in range(1,totalSum+1):
            notTake=dp[index-1][target]
            take=False
            if arr[index]<=target:
                take=dp[index-1][target-arr[index]]
            dp[index][target]=(notTake or take)
    
    mini=10**10
    for target in range(totalSum):
        if dp[n-1][target]:
            s1=target
            s2=totalSum-target
            mini=min(mini,abs(s1-s2))
    return mini