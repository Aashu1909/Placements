# The idea is behind this

class Solution:
    def lcs(self,index1,index2,str1,str2,dp):
        if index1<0 or index2<0:
            return 0
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        if str1[index1]==str2[index2]:
            dp[index1][index2]=1+self.lcs(index1-1,index2-1,str1,str2,dp)
            return dp[index1][index2]
        dp[index1][index2]=max(self.lcs(index1-1,index2,str1,str2,dp),
                               self.lcs(index1,index2-1,str1,str2,dp))
        return dp[index1][index2]
    def lps(self,str1):
        str2=str1[::-1]
        n=len(str1)
        dp=[[-1 for i in range(n+1)] for i in range(n)]
        return self.lcs(n-1,n-1,str1,str2,dp)
    
    def minInsertions(self, s: str) -> int:
        return len(s)-self.lps(s)

obj=Solution()
str1='qjueortjnzdschbrxqattwaasrcnbpjpaetcfechpyxydzeyvieopphkbspcrttaqhzrmimhzzzveikkcmwcfyxrhjlcyxeconuxnqozxjifbeqbitnmxlthlhxuyenombtcryainquxyouxbwbpedaazrsqxfayxvvfuyzhmlkpfkugkohpyshqjouwcyaylcwjaecbnkiltyhikstbfpudzpzwcjkktxqqysvdwbqbflebddapaebxlagmuhugrhirkpxbbsyvlyeptmhlhvlppussacfhrbrctslywaxkdnluejmnfxltbysbcrxjuagxjnvnzzlarwlvjdwxpptalfbrjnpgktmyupfgqmqwiyukfxixwtyhpclrlrwsrnpnfwcmnhdzifdzfcudgnraxkaycsmtmrbtcuxniprjtamegpfvzyodbufklcsdwxvmdqdbhteqayftvhgpriqqdlvhweruiqidpppjoqvcdciqtvlgrkebonythmzsibxwcdlzojfrpfgdnffiqxwtnpcyxncduhqasvfuireqrctvomcxxklkbncbnzkrwrprofuimrtamytygkftqawryvecxjqnquglqtzcyhivqtuyvelqqcnoiiqmjmmdbrxrnyiets'
obj.minInsertions(str1)