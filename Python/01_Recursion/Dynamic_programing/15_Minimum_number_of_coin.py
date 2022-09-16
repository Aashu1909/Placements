# MINIMUM NUMBER OF COINS/COINS CHANGE
# https://practice.geeksforgeeks.org/problems/number-of-coins1824/1
def solve(self,index,coins,amount,dp):
    if index==0:
        if(amount%coins[index]==0):
            return amount//coins[index]
        return 10**9
    if (index,amount) in dp:
        return dp[(index,amount)]
    notTake=0+self.solve(index-1,coins,amount,dp)
    take=10**9
    if coins[index]<=amount:
        take=1+self.solve(index,coins,amount-coins[index],dp)
    dp[(index,amount)]= min(notTake,take)
    return dp[(index,amount)]

def coinChange(self, coins,amount):
    dp={}
    n=len(coins)
    ans=self.solve(n-1,coins,amount,dp) 
    return ans if ans!=10**9 else -1

def coinChange(coins,amount):
    n=len(coins)
    dp=[[0 for _ in range(amount+1)] for _ in range(n)]
    for amt in range(amount+1):
        if(amt%coins[0]==0):
            dp[0][amt]=amt//coins[0]
        else:
            dp[0][amt]=10**9
    
    for index in range(1,n):
        for amt in range(amount+1):
            notTake=0+dp[index-1][amt]
            take=10**9
            if coins[index]<=amt:
                take=1+dp[index][amt-coins[index]]
            dp[index][amt]= min(notTake,take)
    return dp[n-1][amount]