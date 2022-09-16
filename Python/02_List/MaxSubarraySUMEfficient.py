import time
import math
begin=time.time()


def maxSubarraySum(arr):
    n=len(arr)
    maxEnding=arr[0]
    res=-math.inf
    for i in range(1,n):
        maxEnding=max(maxEnding+arr[i],arr[i])
        res=max(res,maxEnding)
    return res
test_case=[1,-2,3,-1,2]
print(maxSubarraySum(test_case))














time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")