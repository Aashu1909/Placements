import time
begin=time.time()

# Ques longest Binaray Subarray woth equal no Zero's One's

def longestSubarray(arr):
    res=0
    n=len(arr)
    for i in range(n):
        countZero=0
        countOne=0
        for j in range(i,n):
            if arr[j]==0:
                countZero+=1
            else:
                countOne+=1      
            if countZero==countOne:
                res=max(res,countZero+countOne)
    return res

#theta(O^2)
#O(1)

time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")