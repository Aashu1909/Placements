def is_Possible(grid):
    #Code here
    def dfs(i,j,n):
        if i<0 or i>=n or j<0 or j>=n or grid[i][j]==0:
            return False
        if grid[i][j]==-1:
            return False
        if grid[i][j]==2:
            return True
        
        grid[i][j]=-1
        
        return dfs(i+1,j,n) or dfs(i-1,j,n) or dfs(i,j+1,n) or dfs(i,j-1,n)
    n=len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                return dfs(i,j,n)