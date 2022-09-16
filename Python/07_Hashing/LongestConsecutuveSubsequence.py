import time
begin=time.time()

#in the naive solution we use sorting
def longestConsecutiveSubsequence(arr):
    arr.sort()
    res,count=1,1
    n=len(arr)
    for i in range(1,n):
        if arr[i]==arr[i-1]+1:
            count+=1
        elif arr[i]!=arr[i-1]:
            res=max(count,res)
            count=1
    return res


test_case=[0]
print(longestConsecutiveSubsequence(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")