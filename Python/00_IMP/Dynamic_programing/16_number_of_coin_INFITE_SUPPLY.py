# https://practice.geeksforgeeks.org/problems/coin-change2448/1?page=2&category[]=Arrays&curated[]=1&sortBy=submissions
# If we have an infinite supply we do not change index when we take 
def solve(self,index,coins,amt,dp):
    if index==0:
        return (amt%coins[0]==0)
    if (index,amt) in dp:
        return dp[(index,amt)]
    # If we are not picking then we chhanges the index
    notTake=0+self.solve(index-1,coins,amt,dp)
    take=0
    if coins[index]<=amt:
        # Not changed the index
        take=self.solve(index,coins,amt-coins[index],dp)
    dp[(index,amt)]=notTake+take
    return dp[(index,amt)]
        
def count(self, coins, n, amt): 
    # code here 
    dp={}
    return self.solve(n-1,coins,amt,dp)
