# KNAPSACK WITH REPITITION  
# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
def knapSack(self, N, W, val, wt):
    # code here
    dp=[[-1 for _ in range(W+1)] for _ in range(N)]
    return self.solve(N-1,W,val,wt,dp)

def solve(self,index,w,val,wt,dp):
    if index==0:
        return (w//wt[0])*val[0]
    if dp[index][w]!=-1:
        return dp[index][w]
    notTake=0+self.solve(index-1,w,val,wt,dp)
    take=-10**9
    if wt[index]<=w:
        take=val[index]+self.solve(index,w-wt[index],val,wt,dp)
    dp[index][w]=max(take,notTake)
    return dp[index][w]