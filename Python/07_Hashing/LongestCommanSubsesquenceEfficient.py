import time
begin=time.time()

def longestCommanSubsequence(arr):
    hashSet=set(arr)
    count=1
    res=1
    for element in hashSet:
        #here we are using element -1 because it indicates the start of new subarrat
        if element-1 not in hashSet:
            #then checking for new subarrays
            curr=1
            while (element+curr) in hashSet:
                curr+=1
            res=max(curr,res)
    return res
test_case=[1,3,9,2,8,2]
print(longestCommanSubsequence(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")