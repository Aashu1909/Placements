# Recursion +memoization
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
def solve(self,index,wt,val,maxW,dp):
    if index==0:
        if wt[index]<=maxW:
            return val[0]
        return 0
    if (index,maxW) in dp:
        return dp[(index,maxW)]
    notTake=0+self.solve(index-1,wt,val,maxW,dp)
    take=-10**9
    if wt[index]<=maxW:
        take=val[index]+self.solve(index-1,wt,val,maxW-wt[index],dp)
    dp[(index,maxW)]=max(take,notTake)
    return dp[(index,maxW)]
    
def knapSack(self,maxW, wt, val, n):
        # code here
        dp={}
        return self.solve(n-1,wt,val,maxW,dp)
        
def zeroOneKnapsack(wt,val,maxW,n):
    dp=[[0 for _ in range(maxW+1)] for i in range(n)]
    for weight in range(n):
        dp[0][weight]=val[0]
    for index in range(n):
        for weight in range(maxW+1):
            notTake=0+dp[index-1][weight]
            take=-10**9
            if wt[index]<=weight:
                take=val[index]+dp[index-1][weight-wt[index]]
            dp[index][weight]=max(take,notTake)
    return dp[n-1][maxW]         

def knapSack(cap, wt,val, n): 
    dp=[0 for _ in range(cap+1)]
    for i in range(n):
        for j in range(cap,wt[i]-1,-1):
            dp[j]=max(dp[j],dp[j-wt[i]]+val[i]);
    return dp[cap]

