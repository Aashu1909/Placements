import time
begin=time.time()

#For the efficent solution we are going to reduce the problem 
#to find the longestSuibarray with ZERO Sum.

def longestSubarraySum(arr,summ):
    #Here we use prefix sum to calculate the longest subarray woth given sum
    # we store the prefix Sum and the index in the hashmap
    # if prefixSum-SUM not in hashmap we insert it with its index
    # otherwise we find the lenght of the subarray with i-hashmap[prefixSum-sum]
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

def longCommanSubWithGivenSum(arr1,arr2):
    #here we first create a temp array which contain 
    # the diffrence of teh element of the two given array
    n,m=len(arr1),len(arr2)
    if n!=m:
        return -1
    
    temp=[0]*n
    for i in range(n):
        temp[i]=arr1[i]-arr2[i]
    #after we create the difference array the problem reduced to longest Subarrray with zero Sum
    return longestSubarraySum(temp,0)

arr1=[0,1,0,0,0,0]
arr2=[1,0,1,0,0,1]
print(longCommanSubWithGivenSum(arr1,arr2))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")