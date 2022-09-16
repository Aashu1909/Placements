# Minimum path to sum to reach the end of the triangle when we can only move down or diagonally
# https://leetcode.com/problems/triangle/
# Recursive +Memoization
def minimumTotal(triangle):
    n=len(triangle)
    i=j=0
    dp={}
    return solve(i,j,n,triangle,dp)

def solve(self,i,j,n,tr):
    if i==n-1:
        return tr[i][j]
    else:
        down=tr[i][j]+self.solve(i+1,j,n,tr)
        diagonal=tr[i][j]+self.solve(i+1,j+1,n,tr)
        return min(down,diagonal)


# tabulization
def triangle(triangle):
    n=len(triangle)
    dp=[[-1 for _ in range(n)]for _ in range(n)]
    for j in range(n):
        dp[n-1][j]=triangle[n-1][j]
    
    for i in range(n-2,-1,-1):
        for j in range(i,-1,-1):
            down=triangle[i][j]+dp[i+1][j]
            diagonal=triangle[i][j]+dp[i+1][j+1]
            dp[i][j]=min(down,diagonal)
    return dp[0][0]