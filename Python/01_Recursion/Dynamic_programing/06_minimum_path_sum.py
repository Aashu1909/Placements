def minPathSum( grid):
    n,m=len(grid),len(grid[0])
    dp={}
    return countMin(n-1,m-1,grid,dp)

# Memoiation
def countMin(i,j,grid,dp):
    if i==0 and j==0:
        return grid[i][j]
    
    if i<0 or j<0:
        return 10**9
    if (i,j) in dp:
        return dp[(i,j)]
    up=grid[i][j]+countMin(i-1,j,grid,dp)
    left=grid[i][j]+countMin(i,j-1,grid,dp)
    dp[(i,j)]=min(up,left)
    return dp[(i,j)]

# Tabulization
def countMinTabulization(grid):
    n,m=len(grid),len(grid[0])
    MAX=10**9
    dp=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                dp[i][j]=grid[i][j]
            up=grid[i][j]
            if i>0:
                up+=dp[i-1][j]
            else:
                up+=MAX
            left=grid[i][j]
            if j>0:
                left+=dp[i][j-1]
            else:
                left+=MAX
            dp[i][j]=min(up,left)
    return dp[n-1][m-1]
