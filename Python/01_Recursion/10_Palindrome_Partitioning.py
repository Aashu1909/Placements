# https://leetcode.com/problems/palindrome-partitioning/

def palindrome_partition(str1):
    result=[]
    partition=[]
    def backtrack(index):
        if index>=len(str1):
            result.append(partition[:])
            return
        for j in range(index,len(str1)):
            temp_str=str1[index:j+1]
            # Checking if the substring is a Palindrome or Not
            if temp_str==temp_str[::-1]:
                partition.append(temp_str)
                # recursion call for j+1 index
                backtrack(j+1)
                partition.pop()
    backtrack(0)
    return result

str1='aab'
print(palindrome_partition(str1))