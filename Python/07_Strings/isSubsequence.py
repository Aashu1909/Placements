import time
begin=time.time()

# Ques Check if a string is Subsequence of Other

# The idea for the naive solution is to generate all the subsequence of the given 
# string and then compare it with the given string s2 subssequence
# Clearly here the time complexiy will be O(2^n*n) ie exponential; 

# We can do this in far better complexity than exponentioal O(n+m) if lenght of both string
def isSubsequence(s1,s2):
    # here s1 is thr given string and we have to find the s2 as a subsequence in s1
    i,j=0,0
    n,m=len(s1),len(s2)
    if n<m:
        return False
    while i<n and j<m:
        if s1[i]==s2[j]:
            j+=1
        i+=1
    return j==m

def isSubsequenceRecursive(s1,s2,n,m):
    if m==0:
        return True
    if n==0:
        return False
    if s1[n-1]==s2[m-1]:
        return isSubsequenceRecursive(s1,s2,n-1,m-1)
    else:
        return isSubsequenceRecursive(s1,s2,n-1,m)


s1="abcdef"
s2="aed"
n,m=len(s1),len(s2)
print(isSubsequence(s1,s2))
print(isSubsequenceRecursive(s1,s2,n,m))



time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")