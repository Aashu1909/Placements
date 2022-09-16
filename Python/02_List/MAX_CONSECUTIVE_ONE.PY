import time
begin=time.time()

# Ques Maximum Cosecutive One
# Naive
def maxConsecutiveOne(arr):
    res=0
    n=len(arr)
    for i in range(n):
        count=0
        for j in range(i,n):
            if arr[j]==1:
                count+=1           
            else:
                break
        res=max(res,count)
    return res

test_case=[0,1,1,1,0,1,1]
print(maxConsecutiveOne(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")