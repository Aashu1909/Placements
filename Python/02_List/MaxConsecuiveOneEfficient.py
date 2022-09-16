import time
begin=time.time()


def MaxConsecutiveOne(arr):
    res=0
    curr=0
    n=len(arr)
    for i in range(n):
        if arr[i]==1:
            curr+=1
        else:
            res=max(curr,res)
            curr=0
    return res
test_case=[0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1]
print(MaxConsecutiveOne(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")