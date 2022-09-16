import time
begin=time.time()

def maxSumCircularSubarray(arr):
    n=len(arr)
    res=arr[0]
    for i in range(n):
        curr_max=arr[i]
        curr_sum=arr[i]
        for j in range(1,n):
            index=(i+j)%n
            curr_sum+=arr[index]
            curr_max=max(curr_max,curr_sum)
        res=max(curr_max,res)
    return res



test_case=[0]
print(maxSumCircularSubarray(test_case))








time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")