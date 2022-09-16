# The questions says that we have to find the all the path in which a boy standing 
# at the left corner of the matrix can reach bottom most right corener of the matrix 
# RECURSION
def uniquePaths(self,m,n):
    if m==0 and n==0:
        return 1
    if m<0 or n<0:
        return 0
    up=uniquePaths(m-1,n)
    left=uniquePaths(m,n-1)
    return (up+left)

# MEMOIZATION
def solve(m,n,dp):
    if m==0 and n==0:
        return 1
    if m<0 or n<0:
        return 0
    if dp[(m,n)]!=-1:
        return dp[(m,n)]
    up=solve(m-1,n,dp)
    left=solve(m,n-1,dp)
    dp[(m,n)]=up+left
    return (up+left)

def UniquePathTabulized(m,n,dp):        
    dp=[[-1 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j]=1     
            else:
                up,right=0,0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    right=dp[i][j-1]
                dp[i][j]=up+right
                
    return dp[m-1][n-1]
