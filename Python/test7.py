def longestSubarray(arr):
    # Write your code here
    count=0
    result=0
    for i in range(1,len(arr)):
        if abs(arr[i-1]-arr[i])<=0:
            count+=1
        else:
            result=max(result,count)
            count=0
    return result

print(longestSubarray([0,1,2,1,2,3]))

