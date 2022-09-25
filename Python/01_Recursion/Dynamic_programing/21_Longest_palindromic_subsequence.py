class Solution:    
    def longestPalindromeSubseq(self, s: str) -> int:
        revStr=s[::-1]
        n=len(s)
        dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.lcs(n-1,n-1,s,revStr,dp)
    
    def lcs(self,index1,index2,str1,str2,dp):
        if index1<0 or index2<0:
            return 0
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        if str1[index1]==str2[index2]:
            dp[index1][index2]=1+self.lcs(index1-1,index2-1,str1,str2,dp)
            return dp[index1][index2]
        #No matching character
        dp[index1][index2]=max(self.lcs(index1-1,index2,str1,str2,dp),
                               self.lcs(index1,index2-1,str1,str2,dp))
        return dp[index1][index2]
    
    def bottomUp(self,s):
        revStr=s[::-1]
        n=len(s)
        dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n):
            dp[i][0]=0
            dp[0][i]=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==revStr[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][n]