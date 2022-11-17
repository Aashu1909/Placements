# How to solve
# Firstly representing in the form of index I1 rep str1 index and vice versa
# If the character at the indexes matches with each other we decrese both index-1
# If the index dosent match then return the maximum of max(f(index1-1,index2),f(index1,index2-1))
# Base case if any of the index is less then zero then return 0
class Solution:
    def lcs(self,index1,index2,str1,str2,dp):
        # Base
        if index1<0 or index2<0:
            return 0
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        
        if str1[index1]==str2[index2]:
            dp[index1][index2]=1+self.lcs(index1-1,index2-1,str1,str2,dp)
            self.s+=str1[index1]
            return dp[index1][index2]
        # Not character are not same
        dp[index1][index2]=max(self.lcs(index1-1,index2,str1,str2,dp),self.lcs(index1,index2-1,str1,str2,dp))
        return dp[index1][index2]

    def longest_comman_subsequence(self,str1,str2):
        n,m=len(str1),len(str2)
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        self.s=""
        return self.lcs(n-1,m-1,str1,str2,dp)

    def topdown(self,str1,str2):
        n,m=len(str1),len(str2)
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for index2 in range(m+1):
            dp[0][index2]=0
        for index1 in range(n+1):
            dp[index1][0]=0
        for index1 in range(1,n+1):
            for index2 in range(1,m+1):
                if str1[index1-1]==str2[index2-1]:
                    dp[index1][index2]=1+dp[index1-1][index2-1]           
                else:
                # Not character are not same
                    dp[index1][index2]=max(dp[index1-1][index2],dp[index1][index2-1])
        return [dp[n][m],dp]
        
    def print_lcs(self,str1,str2):
        n,dp=self.topdown(str1,str2)
        ans=["$"]*n
        index=n-1
        i,j=len(str1),len(str2)
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ans[index]=str1[i-1]
                index-=1
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
        return ''.join(ans)  

obj=Solution()
str1,str2="abcde","ace"
print(obj.longest_comman_subsequence(str1,str2))
print(obj.s)
# print(obj.topdown(str1,str2))
# print(obj.print_lcs(str1,str2))