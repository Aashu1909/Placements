from re import L
import time
begin=time.time()

def maxSubarraySum(arr):
    n=len(arr)
    summ=0
    curr=0
    for i in range(n):
        for j in range(i,n):
            print(arr[j],end=" ")
            curr+=arr[j]
            print(curr)
            summ=max(summ,curr)
        
    return summ

test_case=[1,-2,3,-1,2]
print(maxSubarraySum(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")