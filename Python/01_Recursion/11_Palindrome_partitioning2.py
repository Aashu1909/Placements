
def palindrome_partition2(str1):
    def backtrack(index):
        if index==len(str1):
            return 0
        minCost=10**9
        for j in range(index,len(str1)):
            cost=1+backtrack(j+1)
            minCost=min(minCost,cost)
        return minCost
    
    return backtrack(0) 

def bottomup(str1):
    dp=[0 for _ in range(len(str1)+1)]
    dp[len(str1)]=0
    for i in range(len(str1)-1,-1,-1):
        minCost=10**9
        for j in range(i,len(str1)):
            temp_str=str1[i:j+1]
            if temp_str==temp_str[::-1]:
                cost=1+dp[j+1]
                minCost=min(minCost,cost)
        dp[i]=minCost

    return dp[0]-1