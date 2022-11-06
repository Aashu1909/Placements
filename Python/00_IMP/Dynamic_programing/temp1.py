class Solution:
    def minimumCostPath(self, grid):
        #Code here
        self.max=10**9
        dp={}
        n,m=len(grid),len(grid[0])
        return self.solve(n-1,m-1,grid,dp)
    
    def solve(self,i,j,grid,dp):
        if i==0 and j==0:
            return grid[i][j]
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) :
            return 10000
        
        if (i,j) in dp:
            return dp[(i,j)]
        up=grid[i][j]+self.solve(i-1,j,grid,dp)
        left=grid[i][j]+self.solve(i,j-1,grid,dp)
        right=grid[i][j]+self.solve(i,j+1,grid,dp)
        down=grid[i][j]+self.solve(i+1,j,grid,dp)
        dp[(i,j)]=min(up,left,right,down)
        return dp[(i,j)]

obj=Solution()
4
grid=[[9 ,4 ,9], 
[6 ,7 ,6],
[8 ,3 ,3],
[7 ,4 ,9 ]] 
print(obj.minimumCostPath(grid))
# print(obj.FactDigit(40321))