import time
begin=time.time()

# arr[2,3,-8,7,-1,2,3] 7,-1,2,3 o/p 11
# arr=[5,8,3] o/p 16
# arr=[-6,-1,-8] op -1
# NAIVE SOLUTION O(n^2)
def max_sum_subarray(arr):
    result=arr[0]
    for i in range(len(arr)):
        current_sum=0
        for j in range(i,len(arr)):
            current_sum+=arr[j]
        result=max(result,current_sum)
    return result

# EFFICIENT SOLUTION O(n)
# trick is to compute the sum till (i-1) in advance and compare it with i 
def max_sum_subarray_efficient(arr):
    max_ending=arr[0]
    result=arr[0]
    for i in range(len(arr)):
        max_ending=max(max_ending+arr[i],arr[i])
        result=max(result,max_ending)
    return result

test_case=[2,3,-8,7,-1,2,3]
# print(max_sum_subarray(test_case))
print(max_sum_subarray_efficient(test_case))










time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
