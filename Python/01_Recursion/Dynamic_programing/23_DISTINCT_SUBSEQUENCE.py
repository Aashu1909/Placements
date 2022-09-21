# LEETCODE HARD
# https://leetcode.com/problems/distinct-subsequences/

# Recursion
def distinct_subsequence(s,t):
    def solve(i,j):
        if j<0:
            return 1
        if i<0:
            return 0
        if s[i]==t[j]:
            # We have 2 choice either to take or pass the matched letter of subsequence
            return solve(i-1,j-1)+solve(i-1,j)
        #else 
        return solve(i-1,j)
    n,m=len(s),len(t)
    return  solve(n-1,m-1)

# memoization
def distinct_subsequence(s,t):
    n,m=len(s),len(t)
    dp=[[-1 for _ in range(m)] for _ in range(n)]
    def solve(i,j):
        if j<0:
            return 1
        if i<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==t[j]:
            # We have 2 choice either to take or pass the matched letter of subsequence
            dp[i][j]= solve(i-1,j-1)+solve(i-1,j)
            return dp[i][j]
        #else 
        dp[i][j]= solve(i-1,j)
        return dp[i][j]
    return  solve(n-1,m-1)

# Tabulization
def distinct_subsequence(s,t):
    n,m=len(s),len(t)
    dp=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n+1):
        dp[i][0]=1
    for j in range(1,m+1):
        dp[0][j]=0
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]    
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][m]


s = "rabbbit"
t = "rabbit"
print(distinct_subsequence(s,t))
