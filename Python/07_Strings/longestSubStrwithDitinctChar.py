import time
from unittest import result
begin=time.time()

# Naive Method
def areDistinct(str1,i,j):
    visitedList=[False]*256
    for k in range(i,j+1):
        if visitedList[ord(str1[k])-ord('a')]==True:
            return False
        visitedList[ord(str1[k])-ord('a')]=True
    return True

def longestDistinct(str1):
    n=len(str1)
    result=0
    for i in range(n):
        for j in range(n):
            if areDistinct(str1,i,j):
                result=max(result,i-j+1)
    return result

# Better Solution
def beterLongestDistinct(str1):
    n=len(str1)
    result=0
    for i in range(n):
        visitedArr=[False]*256
        for j in range(i,n):
            if visitedArr[ord(str1[j])-ord('a')]==True:
                break
            else:
                visitedArr[ord(str1[j])-ord('a')]=True
                result=max(result,j-i+1)
    return result

# Efficient Solution
# The idea is to compute MaxEnd(j)
# MaxEnd(j)=Lenght of the longest Substring that has distinct characters and end with j

def efficientLongestDistinct(str1):
    prev=[-1]*256
    n=len(str1)
    i=0
    for j in range(n):
        i=max(i,prev[ord(str[j])-ord('a')]+1)
        maxEnd=j-i+1
        result=max(result,maxEnd)
        prev[ord(str[j])-ord('a')]=j
    return result


# Leetcode solution 
def lengthOfLongestSubstring(self, s: str) -> int:
    n=len(s)
    charSet=set()
    ans=0
    left=0
    
    for right in range(n):
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        ans=max(ans,right-left+1)        
    return ans
    
test_case=[0]
print(solution(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")