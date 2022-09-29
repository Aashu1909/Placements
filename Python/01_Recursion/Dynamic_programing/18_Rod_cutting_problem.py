# You are given a rod of N inches divide the rot such that it can it can sold at a miximum
class Solution:
    def cutRod(self, price, n):
        #code here
        dp=[[-1 for _ in range(n+1)] for _ in range(n)]
        return self.solve(n-1,n,price,dp)
    
    def solve(self,index,target,price,dp):
        if index==0:
            return (price[0]*target)
        if dp[index][target]!=-1:
            return dp[index][target]
        notTake=0+self.solve(index-1,target,price,dp)
        take=(-10**9)
        rodlength=index+1
        if rodlength<=target:
            take=price[index]+self.solve(index,target-rodlength,price,dp)
        dp[index][target]= max(notTake,take)
        return dp[index][target]
    
    def bottom_up(self,price,N):
        dp=[[0 for _ in range(N+1)]for _ in range(N)]
        
        for i in range(N):
            dp[0][i]=i*price[0]
        
        for index in range(1,N):
            for target in range(N+1):
                notTake=dp[index-1][target]
                take=(-10**9)
                rodlength=index+1
                if rodlength<=target:
                    take=price[index]+dp[index][target-rodlength]
                dp[index][target]= max(notTake,take)
        return dp[N-1][N]


obj=Solution()
arr=[1, 5, 8, 9, 10, 17, 17, 20]
print(obj.cutRod(arr,len(arr))) 
print(obj.topDown(arr,len(arr))) 