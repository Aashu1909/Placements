import time
begin=time.time()

# Ques
# test_case
# O/p

def longestSubWithGivenSum(arr1,arr2):
    #for max lenght of the subarray with given comman sum
    res=0
    n,m=len(arr1),len(arr2)
    if n!=m:
        return -1
    for i in range(n):
        sum1,sum2=0,0
        for j in range(i,n):
            sum1+=arr1[j]
            sum2+=arr2[j]
            if sum1==sum2:
                res=max(res,j-i+1)
    return res



arr1=[0,1,0,0,0,0]
arr2=[1,0,1,0,0,1]
print(longestSubWithGivenSum(arr1,arr2))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")