# Recursion+memoization
def minFallingPathSum(self, matrix):
    n,m=len(matrix),len(matrix[0])
    dp={}
    mini=10**9+7
    for j in range(m):
        mini=min(mini,self.solve(n-1,j,matrix,dp))
    return mini

def solve(self,i,j,mat,dp):
    if j<0 or j>=len(mat[0]):
        return 10**9+7
    if i==0:
        return mat[i][j]
    up=mat[i][j]+self.solve(i-1,j,mat,dp)
    left_diagonal=mat[i][j]+self.solve(i-1,j-1,mat,dp)
    right_diagonal=mat[i][j]+self.solve(i-1,j+1,mat,dp)
    return min(up,left_diagonal,right_diagonal)

# Tabulization
def minFallingPathSum(self, matrix) -> int:
    n,m=len(matrix),len(matrix[0])
    if n==1:
        return min(matrix[0])
    dp=[[0 for _ in range(m)]for _ in range(n)]
    for j in range(m):
        dp[0][j]= matrix[0][j]
    for i in range(n):
        for j in range(m):
            up=matrix[i][j]+dp[i-1][j]
            
            left_diagonal=matrix[i][j]
            if j-1>=0:
                left_diagonal+=dp[i-1][j-1]
            else:
                left_diagonal+=10**9+7
                
            right_diagonal=matrix[i][j]
            if j+1<m:
                right_diagonal+=dp[i-1][j+1]
            else:
                right_diagonal+=10**9+7
            mini=min(up,left_diagonal,right_diagonal)
            dp[i][j]=mini
    
    mini=10**9+7
    for j in range(m):
        mini=min(mini,dp[n-1][j])
    return min