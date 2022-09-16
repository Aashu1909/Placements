import time
begin=time.time()

def maxEvenOddSubarray(arr):
    res=1
    n=len(arr)
    for i in range(n):
        curr=1
        for j in range(i+1,n):
            if (arr[j]%2==0 and arr[j-1]%2!=0) or (arr[j]%2!=0 and arr[j-1]%2==0):
                curr+=1
            else:
                break
        res=max(curr,res)
    return res 


test_case=[7,10,13,14]
print(maxEvenOddSubarray(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")