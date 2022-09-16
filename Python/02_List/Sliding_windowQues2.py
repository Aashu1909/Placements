import time
begin=time.time()
# Q.Find if there is a subarray of size k with the given sum
# test_case=[1,8,30,-5,20,7] sum=45 k=3
# O/p   45 (30 -5 20)

def sliding_window(arr,k,sum):
    curr_sum=0
    for i in range(k):
        curr_sum+=arr[i]
    if (curr_sum==sum):
        return True
    for j in range(k,len(arr)):
        curr_sum+=(arr[j]-arr[j-k])
        if (curr_sum==sum):
            return True
    return False
    
test_case=[1,8,30,-5,20,7] 
sum=44
k=3
print(sliding_window(test_case,k,sum))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")