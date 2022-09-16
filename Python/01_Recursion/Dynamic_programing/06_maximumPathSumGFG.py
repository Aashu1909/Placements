
# https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1?page=4&curated[]=1&sortBy=submissions
class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        dp=[[-1 for i in range(N)] for i in range(N)]
        maxSum=0
        for i in range(N):
            positionAns=self.solve(0,i,Matrix,dp)
            maxSum=max(maxSum,positionAns)
        return maxSum
        
    def solve(self,i,j,matrix,dp):
        if j<0 or j>=len(matrix[0]):
            return 0
        if i==N-1:
            return matrix[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        diagonalLeft=matrix[i][j]+self.solve(i+1,j-1,matrix,dp)
        down=matrix[i][j]+self.solve(i+1,j,matrix,dp)
        diagonalRight=matrix[i][j]+self.solve(i+1,j+1,matrix,dp)
        dp[i][j]=max(down,diagonalLeft,diagonalRight)
        return dp[i][j]