def uniquePathsIII(grid):
    end_x,end_y=0,0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                end_x,end_y=i,j
                break
            # elif grid[i][j]==1:
            #     start_x,start_y=i,j
    dp={}
    n,m=len(grid),len(grid[0])
    return countPath(end_x,end_y,n,m,grid,dp)

def countPath(e1,e2,n,m,grid,dp):
    if (e1<0 or e2<0 or grid[e1][e2]==-1 or e1>=n or e2>=m):
        return 0
    if grid[e1][e2]==1:
        return 1
    if (e1,e2) in dp:
        return dp[(e1,e2)]
    
    up=countPath(e1-1,e2,n,m,grid,dp)
    down=countPath(e1+1,e2,n,m,grid,dp)
    left=countPath(e1,e2-1,n,m,grid,dp)
    right=countPath(e1,e2+1,n,m,grid,dp)
    dp[(e1,e2)]= up+down+left+right
    return dp[(e1,e2)]
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(uniquePathsIII(grid))