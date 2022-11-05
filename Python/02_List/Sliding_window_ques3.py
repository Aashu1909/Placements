import time
begin=time.time()
# Q.Given an unsorted of +ve number .Find if there Exist a subarray with given sum
# test_case=[1,4,20,3,10,5] sum=33
# O/p True

def subarray_with_sum_k(arr,sum):
    curr_sum=arr[0]
    start=0
    for end in range(1,len(arr)):
        # we have placed it before adding the 
        while(curr_sum>sum) and start<end:
            curr_sum=curr_sum-arr[start]
            start+=1
        if curr_sum==sum:
            return True
        curr_sum+=arr[end]
    return False

test_case=[1,4,20,3,10,6]
sum=33
print(subarray_with_sum_k(test_case,sum))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")