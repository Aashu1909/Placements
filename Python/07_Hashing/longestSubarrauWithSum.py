import time
begin=time.time()

#theta(N)
#

def longestSubarraySum(arr,summ):
    hashmap={}
    pre_sum=0
    res=0
    n=len(arr)
    for i in range(n):
        pre_sum+=arr[i]
        if pre_sum==summ:
            res=i+1

        if pre_sum not in hashmap:
            hashmap[pre_sum]=i

        if (pre_sum-summ) in hashmap:
            res=max(res,i-hashmap[pre_sum-summ])
    return res


test_case=[5,2,3]
summ=5
print(longestSubarraySum(test_case,summ))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")