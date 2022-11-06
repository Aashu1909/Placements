# https://leetcode.com/problems/palindrome-partitioning/

def palindrome_partition(str1):
    ans=[]
    partition=[]
    def backtrack(index):
        if index==len(str1):
            ans.append(partition[:])
            return 
            
        for j in range(index,len(str1)):
            temp_str=str1[index:j+1]
            if temp_str==temp_str[::-1]:
                partition.append(temp_str)
                backtrack(j+1)
                partition.pop()
    backtrack(0)

    return ans    
str1='aab'
print(palindrome_partition(str1))
# op[[a,a,b],[aa,b]]