import time
from unittest import result
begin=time.time()

# Ques Window sliding technique .We need to find pur the max sum in the given window
# test_case=[1,8,30,-5,20,7] k=3
# O/p   45 (30 -5 20)

def sliding_window(arr,k):
    # Sum for first k element
    curr_sum=0
    for i in range(k):  
        curr_sum+=arr[i]
    max_sum_in_window=curr_sum
    for j in range(k,len(arr)):
        curr_sum+=arr[j]-arr[j-k]
        max_sum_in_window=max(max_sum_in_window,curr_sum)
    return max_sum_in_window

test_case=[1,8,30,-5,20,7]
k=3
print(sliding_window(test_case,k))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")