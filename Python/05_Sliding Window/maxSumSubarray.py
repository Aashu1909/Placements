import time
begin=time.time()

def maxSumSubarray(arr,k):
    window_sum=0
    max_sum=0
    n=len(arr)
    for i in range(k):
        window_sum+=arr[i]
    max_sum=window_sum
    for j in range(k,n):
        window_sum+=arr[j]-arr[j-k]
        max_sum=max(max_sum,window_sum)
    return max_sum

test_case=[100, 200, 300, 400]
print(maxSumSubarray(test_case,2))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")