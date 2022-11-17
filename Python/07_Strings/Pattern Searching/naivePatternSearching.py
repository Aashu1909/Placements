import time
begin=time.time()

# here Time complexity will be O(N^2)
# aux Space will be O(1)

def naivePatternSearching(txt,pat):
    n,m=len(txt),len(pat)
    ans=[]
    if m>n:
        return -1
    for i in range(0,n-m+1):
        print(txt[i:])
        j=0
        while j<m:
            if pat[j]!=txt[i+j]:
                break
            j+=1
        if j==m:
            ans.append(i)
    return ans

txt="abcdaabcd"
pat="abcd"
print(naivePatternSearching(txt,pat))



time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")