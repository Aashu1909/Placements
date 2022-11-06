# Follow up question to the previous one
# what ig any path contain any obstacle 
# here n,m are the last index
# https://leetcode.com/problems/unique-paths-ii/
# RECURSION
from collections import defaultdict
def unique_path(n,m,grid):
    if n==0 and m==0:
        return 1
    if m<0 or n<0 or grid[n][m]==1:
        return 0
    up=unique_path(n-1,m,grid)
    left=unique_path(n,m-1,grid)
    return up+left
# MEMOIZATION
def solve(self,n,m,grid,dp):
    if n==0 and m==0 and grid[0][0]!=1:
        return 1
    if m<0 or n<0 or grid[n][m]==1:
        return 0
    if dp[(n,m)]!=-1:
        return dp[(n,m)]
    up=self.solve(n-1,m,grid,dp)
    left=self.solve(n,m-1,grid,dp)
    dp[(n,m)]=up+left
    return dp[(n,m)]

def uniquePathsWithObstacles(obstacleGrid):
    n,m=len(obstacleGrid),len(obstacleGrid[0])
    dp=defaultdict(lambda:-1)
    return solve(n-1,m-1,obstacleGrid,dp)
