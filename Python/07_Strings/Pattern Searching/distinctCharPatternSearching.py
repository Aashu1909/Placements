from re import L
import time
begin=time.time()

# here Time complexity will be O(N)
# aux Space will be O(1)

# We assume PATTERN has DISTINCT Character
# Time Complexity will be O(n) ``
def DistinctCharPatternSearching(txt,pat):
    n,m=len(txt),len(pat)
    ans=[]
    if m>n:
        return -1
    i=0
    while i<=(n-m):
        j=0
        while j<m:
            if pat[j]!=txt[i+j]:
                break
            j+=1
        if j==m:
            ans.append(j)
        if j==0:
            i+=1
        else:
            i=i+j
    
    return ans

txt="abcdababcd"
pat="abcd"
print(DistinctCharPatternSearching(txt,pat))



time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")